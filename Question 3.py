import turtle

#Get user inputs
branch_length = int(input('Enter length of first branch in pixels:'))
branch_reduction = int(input('Enter percentage (as whole number) to reduce each branch length by:'))
left_branch_angle = int(input('Enter left branch angle:'))
right_branch_angle = int(input('Enter right branch angle:'))
recursion_depth = int(input('Enter number of times to branch:'))

def draw_branch(br_turtle_instance, br_branch_length, br_branch_reduction, br_left_branch_angle, br_right_branch_angle, br_recursion_depth):
    #Once the recursion depth has reached 1, return to previous function
    if br_recursion_depth == 1:
         return
    #On first instance, the current recursion depth countdown will be equal to the recusrion depth entered - in this case, draw the trunk in brown
    if br_recursion_depth == recursion_depth:
        br_turtle_instance.pencolor('brown')
    else:
        br_turtle_instance.pencolor('green') 

    #Draw current branch      
    br_turtle_instance.forward(br_branch_length) 
    
    #Turn to the left in order to draw the next branch
    br_turtle_instance.left(br_left_branch_angle)
    #Initiate new instance to draw new branch to the left
    draw_branch(br_turtle_instance,br_branch_length * (1 - br_branch_reduction / 100), br_branch_reduction, br_left_branch_angle, br_right_branch_angle, br_recursion_depth - 1)

    #After drawing left branch turn back to the right. Angle will be left + right angles, to reverse left turn and initiate right turn
    br_turtle_instance.right(br_left_branch_angle + br_right_branch_angle) 
    #Initiate new instance to draw next branch to the right
    draw_branch(br_turtle_instance,br_branch_length * (1 - br_branch_reduction / 100), br_branch_reduction, br_left_branch_angle, br_right_branch_angle, br_recursion_depth - 1)        
    
    #After drawing right branch, return to centre by reversing right angle
    br_turtle_instance.left(br_right_branch_angle)

    #Except for in first instance, reverse back to start of branch to draw next branch. if statement prevents reversal in first instance to prevent green line overwriting trunk
    if br_recursion_depth != recursion_depth:          
        br_turtle_instance.backward(br_branch_length) 
    
    return

def main():
    
    #Initiate turtle
    turtle_instance = turtle.Turtle() 
    
    #set pen width for turtle
    turtle_instance.width('3')

    #Change angle, so that trunk is drawn vertically
    turtle_instance.left(90) 

    #Initiate drawing of branches
    draw_branch(turtle_instance, branch_length, branch_reduction, left_branch_angle, right_branch_angle, recursion_depth)
    

main()