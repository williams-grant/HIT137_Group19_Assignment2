import os
import re
import pandas as pd
import sqlite3


class Data_Analysis:
    #Use class level variables to make these available to all functions within class through self, rather than needing to pass to every function.
    WORKING_DIRECTORY = os.path.dirname(__file__)
    DIRECTORY = 'temperature_data\\'
    SQL_DB = WORKING_DIRECTORY + '\\a2q2.db'
    SQL_TABLE = 'weather_data'

    def __init__(self):
        #Set up sqlite connection
        self.sql_conn = sqlite3.connect(self.SQL_DB)
        self.cur = self.sql_conn.cursor()
        self.cur.execute('DROP TABLE IF EXISTS ' + self.SQL_TABLE)
        self.sql_conn.commit()

    def getFiles(self):
        #Poll the directory containing csv files and return files as a list
        files = []
        filepath = os.path.join(os.path.dirname(__file__), self.DIRECTORY)
        for filenames in os.listdir(filepath):
            files.append(os.path.join(filepath, filenames))
        return files

    def getyear(self, filename):
        #Each file relates to a year, and the year is contained in the file name. This parses the year out of the filename.
        file = os.path.split(filename)
        return re.findall('(\d+)', file[1])

    def import_data(self, filename, data_year):
        #Use pandas to import csv data into pandas dataframe
        data_to_load = pd.read_csv(filename)
        #Add column to the dataframe containing year previously parsed from filename
        data_to_load['YEAR'] = data_year

        #Unpivot the data and store in a new dataframe
        data_to_load_unpivot = data_to_load.melt(id_vars=['STATION_NAME','STN_ID','LAT','LON','YEAR'],var_name='MONTH',value_name='Temperature')
        #Add an empty column for season to the dataframe
        data_to_load_unpivot['SEASON'] = ''
        #Transfer the unpivoted dataframe to sqlite database
        data_to_load_unpivot.to_sql(self.SQL_TABLE, self.sql_conn, if_exists='append', index=False)

    def update_seasons(self):
        #Update the table in sqlite database to fill in the season column
        update_sql = '''
            UPDATE ''' + self.SQL_TABLE + '''
            SET [SEASON] = CASE WHEN [MONTH] IN ('December', 'January', 'February') THEN 'Summer'
            WHEN [MONTH] IN ('March', 'April', 'May') THEN 'Autumn'
            WHEN [MONTH] IN ('June', 'July', 'August') THEN 'Winter'
            ELSE 'Spring' END
            '''
        self.sql_conn.execute(update_sql)
        self.sql_conn.commit()

    def on_execute(self):
        #Get the list of csv files to be analysed
        filelist = self.getFiles()

        #Import each file to the sqlite database
        for file in filelist:
            year = self.getyear(file)
            self.import_data(file, year[0])

        #Update records in the sqlite database to populate season column
        self.update_seasons()

        #Use SQL/pandas to extract the required data and export to csv
        sql_result = pd.read_sql_query('SELECT STATION_NAME, YEAR, SEASON, ROUND(AVG(Temperature),2) AS [Average Temp] FROM ' + self.SQL_TABLE + ' GROUP BY STATION_NAME, YEAR, SEASON', self.sql_conn)
        sql_result.to_csv(self.WORKING_DIRECTORY + '\\average_temperature.txt', index=False)

        sql_result = pd.read_sql_query('SELECT STATION_NAME, Round(Max(Temperature)-Min(Temperature),2) AS Temperature_Range FROM ' + self.SQL_TABLE + ' GROUP BY STATION_NAME HAVING (((Max([Temperature])-Min([Temperature])) In (SELECT Max(Temperature)-Min(Temperature) AS Temp_Range FROM ' + self.SQL_TABLE + ' GROUP BY STATION_NAME ORDER BY Max(Temperature)-Min(Temperature) DESC LIMIT 1)))', self.sql_conn)
        sql_result.to_csv(self.WORKING_DIRECTORY + '\\largest_temp_range_station.txt', index=False)

        sql_result = pd.read_sql_query('SELECT STATION_NAME, "Warmest" AS DESCRIPTION, Temperature FROM ' + self.SQL_TABLE + ' WHERE Temperature = (SELECT MAX(Temperature) FROM ' + self.SQL_TABLE + ') UNION ALL SELECT STATION_NAME, "Coolest" AS DESCRIPTION, Temperature FROM ' + self.SQL_TABLE + ' WHERE Temperature = (SELECT MIN(Temperature) FROM ' + self.SQL_TABLE + ')', self.sql_conn)
        sql_result.to_csv(self.WORKING_DIRECTORY + '\\warmest_and_coolest_station.txt', index=False)


def main():
    #Initialise new instance of data analysis class
    new_data_analysis = Data_Analysis()
    #Execute functions for instance of data analysis class
    new_data_analysis.on_execute()

#Only run if module is being invoked directly i.e. not being imported by another running module
if __name__ == '__main__':
    main()
