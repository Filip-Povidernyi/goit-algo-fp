import turtle


def draw_pifagor_tree(turtle, branch_length, recursion_level):
    if recursion_level <= 0:
        return
    else:
        turtle.forward(branch_length)
        turtle.left(45)
        draw_pifagor_tree(turtle, 0.8 * branch_length, recursion_level - 1)
        turtle.right(90)
        draw_pifagor_tree(turtle, 0.8 * branch_length, recursion_level - 1)
        turtle.left(45)
        turtle.backward(branch_length)


def main():

    recursion_level = int(input("Введіть рівень рекурсії: "))

    my_turtle = turtle.Turtle()
    my_turtle.speed(250)
    my_turtle.penup()
    my_turtle.goto(0, -200)
    my_turtle.pendown()
    my_turtle.color("green")
    my_turtle.left(90)

    draw_pifagor_tree(my_turtle, 100, recursion_level)
    turtle.exitonclick()


if __name__ == "__main__":
    main()
