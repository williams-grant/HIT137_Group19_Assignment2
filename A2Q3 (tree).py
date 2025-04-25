# import turtle graphic module to use for drawing tree model
import turtle

# Function for drawing tree  using turtle with several arguements for tree criteria
def draw_tree(turtle_instance, branch_length, angle_left, angle_right, reduction_factor, recursion_depth, initial_recursion_depth): 
    # Check recursion depth. If 0, then all requested recursions have occurred and function should return without drawing any further branches.
    if recursion_depth == 0: 
        return

    # Defines the thickness of the trunk and brances based in recursion depth. Higher the number (depth) => closer to the trunk => thicker the line.
    turtle_instance.pensize(recursion_depth)

    # First call with full depth defines our trunk, 'else' statement calls all other recursions are green to define our leafy branches following initial branching
    if recursion_depth == initial_recursion_depth:
        turtle_instance.pencolor("brown")
    else:
        turtle_instance.pencolor("green")

    # Draw the branch
    turtle_instance.forward(branch_length)

    # Change the angle of the turtle using the left angle entered and initiate recursion to draw left branch
    # Note recursion depth is passed decemented by 1. This determines which level of branching is being drawn.
    turtle_instance.left(angle_left)
    draw_tree(turtle_instance, branch_length * reduction_factor, angle_left, angle_right, reduction_factor, recursion_depth - 1, initial_recursion_depth)

    # Change the angle of the turtle to the right angle entered and initiate another recursion to draw right branch.
    # Note that the angle is determined by adding the left and right angles entered - to reverse the precious left angle turn and make the right turn.
    turtle_instance.right(angle_left + angle_right)
    draw_tree(turtle_instance, branch_length * reduction_factor, angle_left, angle_right, reduction_factor, recursion_depth - 1, initial_recursion_depth)

    # Change the angle of the turtle back to centre by reversing the previous change to the right.
    turtle_instance.left(angle_right)

    # Move the cursor back to the start of the current branch in order to draw other branches at same recursion level
    turtle_instance.backward(branch_length)


def main():
    # Use try/except to handle errors e.g. user enters non-numeric character when numeric inputs are required.
    try:
        # Taking user input for required aspects of tree
        angle_left = float(input("Enter left branch angle: "))
        angle_right = float(input("Enter right branch angle: "))
        branch_length = float(input("Enter starting branch length: "))
        reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7 for 70%): "))
        initial_recursion_depth = float(input("Enter number of times to branch out: "))
    
        # Setting up turtle
        # Create turtle instance
        turtle_instance = turtle.Turtle()
        #Bring the turtle screen be to the frontmost window on screen
        turtle_instance.getscreen()._root.attributes('-topmost', True)
        # Set the turtle drawing speed to be fastest
        turtle_instance.speed("fastest")
        # Default turtle drawing position on screen is left to right. Turn turtle 90 degrees to the left to make the tree draw vertically
        turtle_instance.left(90)
    
        #Initiate 
        draw_tree(turtle_instance, branch_length, angle_left, angle_right, reduction_factor, initial_recursion_depth, initial_recursion_depth)

        #Close out turtle
        turtle.done()

    except:
        print('Something went wrong. Exiting...')


# Only run if module is being invoked directly i.e. not being imported by another running module
if __name__ == "__main__":
    main()
