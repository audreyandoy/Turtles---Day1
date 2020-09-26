import turtle

# setup screen from turtle

turtle.title("My Turtle Game")
turtle.bgcolor("white")
turtle.setup(600,600)
turtle.shape("turtle")

screen = turtle.Screen()
john = turtle.Turtle()

input_shape = input("What shape would you like to draw? ")
input_length = input("How big would you like your shape? ")
input_color = input("Choose a color: ")

def triangle(length, color):
    john.fillcolor(color)
    john.begin_fill()
    x = 0
    while x < 3:
        john.forward(int(length))
        john.right(120)
        x = x+1
    john.end_fill()

triangle(input_length, input_color)
