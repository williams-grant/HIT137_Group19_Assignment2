import turtle

def draw_tree(branch_length, angle_left, angle_right, reduction_factor): #Needs one more variable for number of branches remaining
    if reduction_factor == 0: ###This needs to be testing number of branches remaining
        return

    turtle.forward(branch_length)
    turtle.left(angle_left)

    draw_tree(branch_length * reduction_factor, angle_left, angle_right, reduction_factor) ###with additional variable for number of branches remaining, add this to call as number of branches - 1

    turtle.right(angle_left + angle_right)

    draw_tree(branch_length * reduction_factor, angle_left, angle_right, reduction_factor) ###with additional variable for number of branches remaining, add this to call as number of branches - 1

    turtle.left(angle_right)
    turtle.backward(branch_length)

def main():
    # Taking user input
    angle_left = float(input("Enter left branch angle: "))
    angle_right = float(input("Enter right branch angle: "))
    branch_length = float(input("Enter starting branch length: "))
    reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7 for 70%): "))
    ###Need one more input for number of branches (recursion depth)

    # Setting up turtle
    turtle.speed("fastest")
    turtle.left(90)
    turtle.up()
    turtle.goto(0, -200)
    turtle.down()

    draw_tree(branch_length, angle_left, angle_right, reduction_factor)

    turtle.done()

if __name__ == "__main__":
    main()
