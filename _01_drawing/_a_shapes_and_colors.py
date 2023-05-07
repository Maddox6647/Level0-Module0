import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    Chunky_Guy = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    Chunky_Guy.shape("turtle")
    # Set your turtle's speed using .speed(2)
    Chunky_Guy.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    Chunky_Guy.color('lime')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    Chunky_Guy.begin_fill()
    Chunky_Guy.forward(150)
    # Move your turtle left or right using .left(90) or .right(90)
    for i in range(100):
        Chunky_Guy.left(90)
        Chunky_Guy.forward(150)
        Chunky_Guy.left(90)
        Chunky_Guy.forward(150)
        Chunky_Guy.left(90)
        Chunky_Guy.forward(150)
        Chunky_Guy.end_fill()

    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen

    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()

