#import turtle graphic module to use for drawing tree model
import turtle

#Function for drawing tree  using turtle with several arguements for tree criteria
def draw_tree(turtle_instance, branch_length, angle_left, angle_right, reduction_factor, recursion_depth, initial_recursion_depth): 
    if recursion_depth == 0: #Controls how many times branching occurs, will countdown and stop at 0
        return

    #Defines the thickness of the trunk and brances based in recursion depth. Higher the number (depth) => closer to the trunk => thicker the line.
    turtle_instance.pensize(recursion_depth)

    #First call with full depth defines our trunk, 'else' statement calls all other recursions are green to define our leafy branches following initial branching
    if recursion_depth == initial_recursion_depth:
        turtle_instance.pencolor("brown")
    else:
        turtle_instance.pencolor("green")
        
    turtle_instance.forward(branch_length)
    turtle_instance.left(angle_left)

    draw_tree(turtle_instance, branch_length * reduction_factor, angle_left, angle_right, reduction_factor, recursion_depth - 1, initial_recursion_depth)

    turtle_instance.right(angle_left + angle_right)

    draw_tree(turtle_instance, branch_length * reduction_factor, angle_left, angle_right, reduction_factor, recursion_depth - 1, initial_recursion_depth)

    turtle_instance.left(angle_right)
    turtle_instance.backward(branch_length)

def main():
    # Taking user input
    angle_left = float(input("Enter left branch angle: "))
    angle_right = float(input("Enter right branch angle: "))
    branch_length = float(input("Enter starting branch length: "))
    reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7 for 70%): "))
    initial_recursion_depth = float(input("Enter number of times to branch out: "))

    # Setting up turtle
    turtle_instance = turtle.Turtle()
    turtle_instance.getscreen()._root.attributes('-topmost', True)
    turtle_instance.speed("fastest")
    turtle_instance.left(90)
    turtle_instance.up()
    turtle_instance.goto(0, -200)
    turtle_instance.down()

    draw_tree(turtle_instance, branch_length, angle_left, angle_right, reduction_factor, initial_recursion_depth, initial_recursion_depth)

    turtle.done()

if __name__ == "__main__":
    main()
