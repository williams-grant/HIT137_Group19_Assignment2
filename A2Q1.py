#Assignment 2 Q1
#Read a raw text file, envrypt text create new file, then decrypte and check decryption returns original text

#import os scipt to allow program to search for raw_text.txt and create and name file once encrypted and decrypted
import os

#use encrypt funciton to read whole text within raw_text.txt file.Use parameter, n and m as user inputs for the encryption logic below. 
#Parameter = original_text to read whole string
def encrypt(original_text, n, m):
    encrypted_text = ''  #Stores encrypted text 
    key_text = ''  #assigns a key to each character based on each encryption logic to allow for cleaner decryption,
    # avoiding decryption logic issues if esperate encryption logics result in the same character

    # loops though each character in the string
    for char_to_encrypt in original_text: 
        
        # if character is in range a to m, shift forward by (n*m) then return a character based on encryption logic. Mark character with '1' to indicate which rule was used
        if 'a' <= char_to_encrypt <= 'm':
            encrypted_char = chr(ord('a') + (ord(char_to_encrypt) - ord('a') + (n * m)) % 26)
            key_char = '1'

        #if character is in range n to z, shift backwards by (n + m) then return character based on encrpytion logic. Mark character with '2' to indicate logic used
        elif 'n' <= char_to_encrypt <= 'z': 
            encrypted_char = chr(ord('a') + (ord(char_to_encrypt) - ord('a') - (n + m)) % 26)
            key_char = '2'

        #if character is in range A to M, shift backwards by ( - n) then return character based on encryption logic. Mark character with '3' to indicate logic used
        elif 'A' <= char_to_encrypt <= 'M':  
            encrypted_char = chr(ord('A') + (ord(char_to_encrypt) - ord('A') - n) % 26)
            key_char = '3'
            
        #if character is in range N to Z, shift forward by (m^2) then return charter based on encryption logic. Mark character with '3' to inidcate logic used
        elif 'N' <= char_to_encrypt <= 'Z':  
            encrypted_char = chr(ord('A') + (ord(char_to_encrypt) - ord('A') + (m**2)) % 26) 
            key_char = '4'

        #All other charcters, remain the same and mark with '0'
        else:
            encrypted_char = char_to_encrypt
            key_char = '0'

        #returns transformed characters to a result string as encrypted_text and stores key codes in key_text
        encrypted_text += encrypted_char
        key_text += key_char
    return encrypted_text, key_text


#Use decrypt function to decrypt 'encrypted_text' file and key codes in key_text to indicate which decryption logic to use 
def decrypt(encrypted_text, key_text, n, m):
    decrypted_text = '' #stores decrypted text

    #Each character from 0 to the length of the string (i.e. encrypted_text) is assigned a position.
    #This allows the program to access both strings at the same time, pulling from encryped_text and key_text at each character position
    for char_pos in range(0, len(encrypted_text)):
        char_to_decrypt = encrypted_text[char_pos]
        key_char = key_text[char_pos]

        #Uses decryption logic based on key code, to reverse encryption formula. Shifting backwards by (n*m)
        if key_char == '1':
            decrypted_char = chr(ord('a') + (ord(char_to_decrypt) - ord('a') - (n * m)) % 26)
            
        #if key is not 1, 'else if' statement tells program to move and decrypt based on key code. Shifting forwards by (n+m)
        elif key_char == '2': 
            decrypted_char = chr(ord('a') + (ord(char_to_decrypt) - ord('a') + (n + m)) % 26)
            
        #if key code is 3, use below decyription logic to shift forward by ( +n)
        elif key_char == '3':  
            decrypted_char = chr(ord('A') + (ord(char_to_decrypt) - ord('A') + n) % 26)
        #if key code is 4, use below decryption logic to shift backwards by (m^2)
        elif key_char == '4':  
            decrypted_char = chr(ord('A') + (ord(char_to_decrypt) - ord('A') - (m**2)) % 26)   
        #if key code is not 1-4 then return same character in decryption_text
        else:
            decrypted_char = char_to_decrypt
        #gives a resulting decryption string, and returns as decryption_text
        decrypted_text += decrypted_char 
    return decrypted_text


def readFile(directory, filename):
    #build os filepath using directory and filename passed
    file_to_read = os.path.join(directory, filename)
    #'with' statment ensures file is closed after function completed - even if error occurs reduces chance of data loss
    with open(file_to_read, 'r', encoding='utf-8') as file:
        return file.read()


def writeFile(text_to_write, directory, filename):
    #Save the key_text to a seperate file - in case error occurs still have code to use decryption logic
    file_to_write = os.path.join(directory, filename)
    with open(file_to_write, 'w', encoding='utf-8') as file:
        file.write(text_to_write)


def process_encryption(m, n):
    #Read original text file and load into variable
    original_text = readFile(os.path.dirname(__file__), 'raw_text.txt')

    #Uses our custom encryption function as defined above
    encrypted_text, key_text = encrypt(original_text, m, n)

    #Write the encrypted text to a new file
    writeFile(encrypted_text, os.path.dirname(__file__), 'encrypted_text.txt')
            
    #Save the key_text to a seperate file - in case error occurs still have code to use decryption logic
    writeFile(key_text, os.path.dirname(__file__), 'key_text.txt')

    return original_text


def process_decryption(m, n):
    #Read the encrypted text from file
    encrypted_text_from_file = readFile(os.path.dirname(__file__), 'encrypted_text.txt')

    #Read the key text from file
    key_text_from_file = readFile(os.path.dirname(__file__), 'key_text.txt')

    #Uses custom decryption it using the saved key and encrypted text
    decrypted_text = decrypt(encrypted_text_from_file, key_text_from_file, m, n)

    #Save the decrypted text to file 'decrypted_text.txt'
    writeFile(decrypted_text, os.path.dirname(__file__), 'decrypted_text.txt')

    return decrypted_text


def check_decryption(original_text, decrypted_text):
    return original_text == decrypted_text


def main():
    try:
        #Get user imputs
        #Requires value for m and n as an integer - which are used as parameters for the encryption function
        m = int(input('Enter the value for m: '))
        n = int(input('Enter the value for n: '))
    
        if not(isinstance(m, int)) or not(isinstance(n, int)):
           print('Non-integer was entered. Exiting.')
           return
    
        original_text = process_encryption(m, n)

        decrypted_text = process_decryption(m, n)
    
        #Verifies that decryption was successfull by printing true if text are matching
        if check_decryption(original_text, decrypted_text):
            print('Encryption and decryption successful.')
        else:
            print('Decrypted text does not match original text. Encryption and decryption unsuccessful')
    except:
        print('Something went wrong. Exiting...')
        
#Only run if module is being invoked directly i.e. not being imported by another running module
if __name__ == '__main__':
    main()
