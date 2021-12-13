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

#Create a turtle object to draw the labels on the board
letter_drawer = trtl.Turtle()

#Define the board drawer's initial attributes
board_drawer_shape = "classic"
board_drawer_pencolor = "black"
board_drawer_fillcolor = "black"
board_drawer_shapesize = 1
board_drawer_speed = 0
board_drawer_initial_heading = 0
board_drawer_initial_x_position = -260
board_drawer_initial_y_position = -260

#Define the letter drawer's initial attributes
letter_drawer_shape = "classic"
letter_drawer_pencolor = "black"
letter_drawer_fillcolor = "black"
letter_drawer_shapesize = 1
letter_drawer_speed = 0
letter_drawer_initial_heading = 0
letter_drawer_initial_x_position = -228
letter_drawer_initial_y_position = -280

#Define the chess board's initial attributes
number_of_sides = 4
number_of_squares = 64
number_of_squares_on_side = number_of_squares / 8
length_of_side = 520
length_of_square = length_of_side / 8

#Give the board drawer its defined attributes
board_drawer.shape(board_drawer_shape)
board_drawer.pencolor(board_drawer_pencolor)
board_drawer.fillcolor(board_drawer_fillcolor)
board_drawer.shapesize(board_drawer_shapesize)
board_drawer.speed(board_drawer_speed)
board_drawer.penup()
board_drawer.setheading(board_drawer_initial_heading)
board_drawer.goto(board_drawer_initial_x_position, board_drawer_initial_y_position)

#Give the letter drawer its defined attributes
letter_drawer.shape(letter_drawer_shape)
letter_drawer.pencolor(letter_drawer_pencolor)
letter_drawer.fillcolor(letter_drawer_fillcolor)
letter_drawer.shapesize(letter_drawer_shapesize)
letter_drawer.speed(letter_drawer_speed)
letter_drawer.penup()
letter_drawer.setheading(letter_drawer_initial_heading)
letter_drawer.goto(letter_drawer_initial_x_position, letter_drawer_initial_y_position)

#####-Functions-#####
#Define a function to draw a chessboard
def draw_board():
    #Output debug message
    print("drawing the board")

    #For loop to draw the chess board
    for i in range(number_of_sides):
        #Ensure the pen is down because the trails will make the board
        board_drawer.pendown()

        #Grab the current heading of the board
        current_heading = board_drawer.heading()
        
        #Draw the "square" lines on the first two iterations
        if i < 2:
            #For loop to draw all 64 squares in the chess board
            for x in range(int(number_of_squares_on_side)): #This variable can not be i or else it interferes with the outer for loop
                board_drawer.pendown() #Ensure the pen is down because the trails will make the board

                #Draw lines through the middle of the board every square
                board_drawer.forward(length_of_square)
                board_drawer.setheading(current_heading + 90)
                board_drawer.forward(length_of_side)
                board_drawer.back(length_of_side)
                board_drawer.setheading(current_heading)
        
        #Don't need to redraw the square lines, so just draw the frame
        else:
            #Only draw the frame
            board_drawer.forward(length_of_side)

        #Set a new heading
        new_heading = board_drawer_initial_heading + ((i + 1) * 90)
        board_drawer.setheading(new_heading)
    
    #Hide the board drawing turtle when it is done drawing the board
    board_drawer.hideturtle()



#Define a function to give a chessboard labels
def draw_labels():
    #Output a message for debugging
    print("Drawing the labels")

    #For loop to draw all of the letters and numbers on the board
    for i in range(number_of_sides):
        #Check if the turtle is drawing labels on the bottom side of the board
        if i < 1:
            #Output a message for debugging
            print("Draw the letters on the bottom")

        #Check if the turtle is drawing labels on the right side of the board
        elif i < 2:
            #Output a message for debugging
            print("Draw the numbers on the right side")

        #Check if the turtle is drawing labels on the top side of the board
        elif i < 3:
            #Output a message for debugging
            print("Draw the letters on the top side")

        #Check if the turtle is drawing labels on the left side of the board
        else:
            #Output a message for debugging
            print("Draw the numbers on the left side")

    #Ensure the pen is down because the trails will make the board
    letter_drawer.pendown()

#Define a function to draw a full chessboard with labels
def draw_chessboard():
    #Draw the chessboard
    draw_board()

    #Label the chessboard
    draw_labels()