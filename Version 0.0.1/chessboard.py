'''
PLTW Lesson 1.2.5
@authors: Ethan Francolla
'''

#####-Imports-#####
#Import Turtle library for drawing and display functions
import turtle as trtl

#####-Setup-#####
#Create a turtle object to draw the board
board_drawer = trtl.Turtle()

#Define the board drawer's initial attributes
board_drawer_shape = "classic"
board_drawer_pencolor = "black"
board_drawer_fillcolor = "black"
board_drawer_shapesize = 1
board_drawer_speed = 5
board_drawer_initial_heading = 0
board_drawer_initial_x_position = -260
board_drawer_initial_y_position = -260

#Define the chess board's initial attributes
number_of_sides = 4
length_of_side = 520

#Give the board drawer its defined attributes
board_drawer.shape(board_drawer_shape)
board_drawer.pencolor(board_drawer_pencolor)
board_drawer.fillcolor(board_drawer_fillcolor)
board_drawer.shapesize(board_drawer_shapesize)
board_drawer.speed(board_drawer_speed)
board_drawer.penup()
board_drawer.setheading(board_drawer_initial_heading)
board_drawer.goto(board_drawer_initial_x_position, board_drawer_initial_y_position)

#####-Functions-#####
#Define a function to draw a chessboard
def draw_board():
    #Output debug message
    print("drawing the board")

    #For loop to draw the chess board
    for i in range(number_of_sides):
        #Ensure the pen is down because the trails will make the board
        board_drawer.pendown()

        #Draw the frame of the board
        board_drawer.forward(length_of_side)

        #Set a new heading
        board_drawer.setheading(board_drawer_initial_heading + (i + 1) * 90)

#Define a function to give a chessboard labels
def draw_labels():
    print("Drawing the labels")

#Define a function to draw a full chessboard with labels
def draw_chessboard():
    draw_board()
    draw_labels()