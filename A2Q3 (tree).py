import turtle

def draw_tree(branch_length, angle_left, angle_right, reduction_factor, recursion_depth, initial_recursion_depth): 
    if recursion_depth == 0: 
        return

    turtle.pensize(recursion_depth)
    if recursion_depth == initial_recursion_depth:
        turtle.pencolor("brown")
    else:
        turtle.pencolor("green")
        
    turtle.forward(branch_length)
    turtle.left(angle_left)

    draw_tree(branch_length * reduction_factor, angle_left, angle_right, reduction_factor, recursion_depth - 1, initial_recursion_depth)

    turtle.right(angle_left + angle_right)

    draw_tree(branch_length * reduction_factor, angle_left, angle_right, reduction_factor, recursion_depth - 1, initial_recursion_depth)

    turtle.left(angle_right)
    turtle.backward(branch_length)

def main():
    # Taking user input
    angle_left = float(input("Enter left branch angle: "))
    angle_right = float(input("Enter right branch angle: "))
    branch_length = float(input("Enter starting branch length: "))
    reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7 for 70%): "))
    initial_recursion_depth = float(input("Enter number of times to branch out: "))

    # Setting up turtle
    turtle.speed("fastest")
    turtle.left(90)
    turtle.up()
    turtle.goto(0, -200)
    turtle.down()

    draw_tree(branch_length, angle_left, angle_right, reduction_factor, initial_recursion_depth, initial_recursion_depth)

    turtle.done()

if __name__ == "__main__":
    main()
