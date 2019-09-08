######################################################################
# Author: Abraham Moreno
# Username: morenoa2
######################################################################
import turtle

# creates a graphics window
wn = turtle.Screen()

# width is 90% of screen, height is 80% of screen. Screen appears at the center of screen
wn.setup(width=0.9, height=0.8, startx=None, starty=None)

# gets 90% of width and 80% of height of window
widthOfConsole = wn.window_width() * 0.9
heightOfConsole = wn.window_height() * 0.8

# makes all the turtles to be used
outerOne = turtle.Turtle()
toolBar = turtle.Turtle()
toolBarButtons = turtle.Turtle()
text = turtle.Turtle()

# puts all turtles, colors, and letters into lists
myTurtles = [outerOne, toolBar, toolBarButtons, text]
myToolColors = ["#ed2121", "#ffb41f", "#0da310"]
myTextColors = ["white", "#1566ad", "white"]
myTextSigns = [":", "~", "$"]
personSentence = ["a", "b", "e", "@", "u", "b", "u", "n", "t", "u"]

def moveTurtleToTopRight(turtle):
    """
    Moves the turtle to the top right of the "console"
    """

    # moves all turtles to the top right and sets their speed
    turtle.speed(10)
    turtle.penup()
    turtle.forward(widthOfConsole / 2)
    turtle.left(90)
    turtle.forward((heightOfConsole / 2) - 10)
    turtle.circle(10, 90)
    turtle.pendown()
    turtle.begin_fill()

def makeMyConsole():
    """
    Makes the whole "console" square
    """
    outerOne.fillcolor("#360101")
    toolBar.fillcolor("#212121")

    # makes the big square
    for i in range(2):
        outerOne.forward(widthOfConsole)
        outerOne.circle(10, 90)
        outerOne.forward(heightOfConsole)
        outerOne.circle(10, 90)
    outerOne.end_fill()

    # makes the toolbar
    toolBar.forward(widthOfConsole)
    toolBar.circle(10, 90)
    toolBar.forward(30)
    toolBar.left(90)
    toolBar.forward(widthOfConsole + 20)
    toolBar.left(90)
    toolBar.forward(30)
    toolBar.circle(10, 90)
    toolBar.end_fill()

    # calls the makeToolBarButtons function
    makeToolBarButtons()

def makeToolBarButtons():
    """
    Makes the toolbar buttons
    """
    # moves the turtle to position to make the circles
    toolBarButtons.forward(widthOfConsole)
    toolBarButtons.circle(10, 90)
    toolBarButtons.forward(10)
    toolBarButtons.left(90)
    toolBarButtons.shape("circle")
    toolBarButtons.pensize(10)

    # makes the 3 buttons
    for buttons in range(0, len(myToolColors)):
        toolBarButtons.penup()

        # sets the color of the buttons to the turtle by going through each color
        toolBarButtons.color(myToolColors[buttons])

        toolBarButtons.forward(30)
        toolBarButtons.pendown()
        toolBarButtons.stamp()

    # calls the prepareTheText function
    prepareTheText()

def prepareTheText():
    """
    Makes the text that appears
    """
    # sends the turtle into position
    text.forward(widthOfConsole)
    text.circle(10, 90)
    text.forward(55)
    text.left(90)
    text.forward(15)
    text.penup()
    text.pencolor("#007d02")

    # types out each letter
    for letter in range(0, len(personSentence)):
        text.write(personSentence[letter], move=False, align='center', font=("Arial", 10, ("bold", "normal")))
        text.forward(10)

    # types out each sign after the text along with their colors
    for each in range(0, 3):
        text.pencolor(myTextColors[each])
        text.write(myTextSigns[each], move=False, align='center', font=("Arial", 10, ("bold", "normal")))
        text.forward(10)

    # makes the typing box
    text.forward(10)
    text.right(90)
    text.forward(2)
    text.left(90)
    text.color("white")
    text.pendown()
    for i in range(0, 2):
        text.left(90)
        text.forward(20)
        text.left(90)
        text.forward(10)

    # sends the turtle to the center
    text.penup()
    text.setpos(0, 0)

    # sends the turtle to the top right
    moveTurtleToTopRight(text)

def main():
    """
    The main function
    """
    # moves each turtle to the top right
    for eachTurtle in myTurtles:
        moveTurtleToTopRight(eachTurtle)

    # calls makeMyConsole
    makeMyConsole()

# calls the main function
main()

# when user clicks the screen or anything, the program closes
wn.exitonclick()                        # Closes the program when a user clicks in the window