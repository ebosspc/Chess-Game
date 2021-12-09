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
board_drawer.hideturtle()

#Create a turtle object to draw the labels on the board
label_drawer = trtl.Turtle()
label_drawer.hideturtle()

#Define a list of letters that will be used to label the chess board
chessboard_letters_list = ["A","B","C","D","E","F","G","H"]

#Define a list of numbers that will be used to label the chess board
chessboard_numbers_list = ["1","2","3","4","5","6","7","8"]

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
label_drawer_shape = "classic"
label_drawer_pencolor = "black"
label_drawer_fillcolor = "black"
label_drawer_shapesize = 1
label_drawer_speed = 0
label_drawer_initial_heading = 0
label_drawer_initial_x_position = -228
label_drawer_initial_y_position = -295

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
label_drawer.shape(label_drawer_shape)
label_drawer.pencolor(label_drawer_pencolor)
label_drawer.fillcolor(label_drawer_fillcolor)
label_drawer.shapesize(label_drawer_shapesize)
label_drawer.speed(label_drawer_speed)
label_drawer.penup()
label_drawer.setheading(label_drawer_initial_heading)
label_drawer.goto(label_drawer_initial_x_position, label_drawer_initial_y_position)

#####-Functions-#####
#Define a function to draw a chessboard
def draw_board():
    board_drawer.showturtle()
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
    label_drawer.showturtle()
    #Output a message for debugging
    print("Drawing the labels")

    #For loop to draw all of the letters and numbers on the board
    for i in range(number_of_sides):
        #Check if the turtle is drawing labels on the bottom side of the board
        if i < 1:
            #Output a message for debugging
            print("Draw the letters on the bottom")

            #For loop to label the bottom row of the chessboard with letters
            for x in range(int(number_of_squares_on_side)): 
                #Write the appropirate letter from the list of letters with the index of x
                label_drawer.write(chessboard_letters_list[x], align = "center", font = ("Times New Roman", 20, "normal"))

                #Move forward
                label_drawer.forward(length_of_square)

        #Check if the turtle is drawing labels on the right side of the board
        elif i < 2:
            #Output a message for debugging
            print("Draw the numbers on the right side")

            #Move and turn the labeler turtle to the appropriate position
            label_drawer.setheading(180)
            label_drawer.forward(10)
            label_drawer.setheading(90)
            label_drawer.forward(50)

            #For loop to lable the right side of the chessboard with numbers
            for x in range(int(number_of_squares_on_side)):
                #Write the appropirate number from the list of numbers with the index of x
                label_drawer.write(chessboard_numbers_list[x], align = "center", font = ("Times New Roman", 20, "normal"))

                #Move forward
                label_drawer.forward(length_of_square)

        #Check if the turtle is drawing labels on the top side of the board
        elif i < 3:
            #Output a message for debugging
            print("Draw the letters on the top side")

            #Move and turn the labeler turtle to the appropriate position
            label_drawer.goto(-228, 260)
            label_drawer.setheading(0)

            #For loop to label the bottom row of the chessboard with letters
            for x in range(int(number_of_squares_on_side)):
                #Write the appropirate letter from the list of letters with the index of x
                label_drawer.write(chessboard_letters_list[x], align = "center", font = ("Times New Roman", 20, "normal"))

                #Move forward
                label_drawer.forward(length_of_square)

        #Check if the turtle is drawing labels on the left side of the board
        else:
            #Output a message for debugging
            print("Draw the numbers on the left side")

            #Move and turn the labeler turtle to the appropriate position
            label_drawer.goto(-275, -245)
            label_drawer.setheading(90)

            #For loop to label the bottom row of the chessboard with letters
            for x in range(int(number_of_squares_on_side)):
                #Write the appropirate letter from the list of letters with the index of x
                label_drawer.write(chessboard_numbers_list[x], align = "center", font = ("Times New Roman", 20, "normal"))

                #Move forward
                label_drawer.forward(length_of_square)

    #Ensure the pen is down because the trails will make the board
    label_drawer.pendown()

    #Hide the label drawing turtle when it is done drawing the labels
    label_drawer.hideturtle()

#Define a function to draw a full chessboard with labels
def draw_chessboard():
    #Draw the chessboard
    draw_board()

    #Label the chessboard
    draw_labels()
