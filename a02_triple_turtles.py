######################################################################
# Author: Emily Lovell & Scott Heggen              TODO: Change this to your name, if modifying
# Username: lovelle & heggens                     TODO: Change this to your username, if modifying
#

# Assignment: A02: Exploring Turtles in Python
# Purpose: Draws a 3D cube using turtles and nested for loops
######################################################################
# Acknowledgements:

# Original code by: Dr. Scott Heggen

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################
import turtle                           # allows us to use the turtles library

wn = turtle.Screen()                    # creates a graphics window

box_turtle = turtle.Turtle()            # create a turtle named myturtle
box_turtle.speed(10)
box_turtle.penup()
box_turtle.shape('circle')              # possible shapes are 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
height = 100
width = 100
depth = 15

# All the colors to use; the rows loop will select a color on each iteration
colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']

for row in range(6):                    # Loop for the rows
    box_turtle.color(colors[row])       # Set the turtles color on each row
    for col in range(6):                # Loop for the columns
        for dep in range(6):            # Loop for the depth
            # Moves box_turtle to a position based on row, col, and dep
            box_turtle.goto(col * width - 300 + dep * depth, row * height - 300 + dep * depth * 1.2)
            box_turtle.stamp()          # Stamps the shape onto the window

wn.exitonclick()                        # Closes the program when a user clicks in the window
