import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Indian Flag")
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Create a turtle object
flag_turtle = turtle.Turtle()
flag_turtle.speed(10)

# Function to draw a rectangle
def draw_rectangle(color, width, height):
    flag_turtle.begin_fill()
    flag_turtle.color(color)
    for _ in range(2):
        flag_turtle.forward(width)
        flag_turtle.right(90)
        flag_turtle.forward(height)
        flag_turtle.right(90)
    flag_turtle.end_fill()

# Function to draw the Ashoka Chakra
def draw_ashoka_chakra(radius):
    flag_turtle.penup()
    flag_turtle.goto(0, -7)  # Center the Ashoka Chakra in the middle of the white stripe
    flag_turtle.pendown()
    flag_turtle.color("navy")
    for _ in range(24):
        flag_turtle.forward(radius)
        flag_turtle.backward(radius)
        flag_turtle.left(15)
    flag_turtle.penup()
    flag_turtle.goto(0, -28)
    flag_turtle.pendown()
    flag_turtle.circle(radius)

# Move the turtle to the starting position for the saffron rectangle
flag_turtle.penup()
flag_turtle.goto(-200, 100)
flag_turtle.pendown()

# Draw the saffron rectangle
draw_rectangle("orange", 400, 70)

# Move the turtle to the starting position for the white rectangle
flag_turtle.penup()
flag_turtle.goto(-200, 30)
flag_turtle.pendown()

# Draw the white rectangle
draw_rectangle("white", 400, 70)

# Draw the Ashoka Chakra in the center of the white rectangle
draw_ashoka_chakra(20)

# Move the turtle to the starting position for the green rectangle
flag_turtle.penup()
flag_turtle.goto(-200, -40)
flag_turtle.pendown()

# Draw the green rectangle
draw_rectangle("green", 400, 70)

# Hide the turtle
flag_turtle.hideturtle()

# Keep the window open until clicked
turtle.done()
