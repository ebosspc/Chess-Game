'''
PLTW Lesson 1.2.5
@authors: Ethan Francolla
'''

#####-Welcome-#####
#Import abstracted welcome module that will handle giving a user instructions
import welcome as welcome

#Welcome the user to the game in the terminal
welcome.welcome_user()

#Create a variable to track whether the user wants to run the program as a developer to receive helpful debugging messages
#It is off by default
developer_mode = 0

#Ask the user if they want instructions until they enter a valid input
while (True):
    #Store the user input in a variable
    instructions_request = str(input("Please write y for yes, n for no, and d for developer mode: "))

    #Check if the user selected yes and adjust variables appropriately
    if instructions_request == "y":
        instructions_request = 1
        break

    #Check if the user selected no and adjust variables appropriately
    elif instructions_request == "n":
        instructions_request = 0
        break
    
    #Check if the user wants to enter developer mode
    elif instructions_request == "d":
        #Turn on developer mode
        developer_mode = 1
        print("You are now in developer mode.")
        
    #Output an error message if the user enters an invalid input
    else:
        print("Sorry! That was not a valid input.\nPlease try again.")

#Print the instructions if the user wants them
if instructions_request == 1:
    welcome.print_instructions()

#Don't print the instructions if the user doesn't want them
elif instructions_request == 0:
    print("Welcome back!")

#Inform the user the game is starting
print("Lets start the game!")

#Inform the user if they are running the program as a developer
if developer_mode == 1:
    print("You are running this program as a developer.")

#####-Imports-#####
#Import Turtle library for drawing and display functions
import turtle as trtl

#Import abstracted chessboard module for drawing a chessboard
import chessboard as chessboard

#####-Game Config-#####
#Define a list that contains a string corresponding to a specific square on a chessboard
possible_squares_list = ["a1","a2","a3","a4","a5","a6","a7","a8","b1","b2","b3","b4","b5","b6","b7","b8",
"c1","c2","c3","c4","c5","c6","c7","c8","d1","d2","d3","d4","d5","d6","d7","d8",
"e1","e2","e3","e4","e5","e6","e7","e8","f1","f2","f3","f4","f5","f6","f7","f8",
"g1","g2","g3","g4","g5","g6","g7","g8","h1","h2","h3","h4","h5","h6","h7","h8"]

#Generate a screen for the game to diplay on
wn = trtl.Screen()

#Output mesage for debugging if the user is in developer mode
if developer_mode == 1:
    print("Importing and adding gifs")

#Import gifs that will be used as the pawns' shapes
white_pawn_image = "white_pawn.gif"
wn.addshape(white_pawn_image)
black_pawn_image = "black_pawn.gif"
wn.addshape(black_pawn_image)

#Import gifs that will be used as the rooks' shapes
white_rook_image = "white_rook.gif"
wn.addshape(white_rook_image)
black_rook_image = "black_rook.gif"
wn.addshape(black_rook_image)

#Import gifs that will be used as the knights' shapes
white_knight_image = "white_knight.gif"
wn.addshape(white_knight_image)
black_knight_image = "black_knight.gif"
wn.addshape(black_knight_image)

#Import gifs that will be used as the bishops' shapes
white_bishop_image = "white_bishop.gif"
wn.addshape(white_bishop_image)
black_bishop_image = "black_bishop.gif"
wn.addshape(black_bishop_image)

#Import gifs that will be used as the queens' shapes
white_queen_image = "white_queen.gif"
wn.addshape(white_queen_image)
black_queen_image = "black_queen.gif"
wn.addshape(black_queen_image)

#Import gifs that will be used as the kings' shapes
white_king_image = "white_king.gif"
wn.addshape(white_king_image)
black_king_image = "black_king.gif"
wn.addshape(black_king_image)

#Output a message for debugging if the user is in developer mode
if developer_mode == 1:
    print("Defining chessboard initial attributes")

#Define the chess board's initial attributes
number_of_sides = 4
number_of_squares = 64
number_of_squares_on_side = number_of_squares / 8
length_of_side = 520
length_of_square = length_of_side / 8

#Define a tracker variable for each square that indicate whether or not there is a piece on each square
piece_on_a1 = 0
piece_on_a2 = 0
piece_on_a3 = 0
piece_on_a4 = 0
piece_on_a5 = 0
piece_on_a6 = 0
piece_on_a7 = 0
piece_on_a8 = 0
piece_on_b1 = 0
piece_on_b2 = 0
piece_on_b3 = 0
piece_on_b4 = 0
piece_on_b5 = 0
piece_on_b6 = 0
piece_on_b7 = 0
piece_on_b8 = 0
piece_on_c1 = 0
piece_on_c2 = 0
piece_on_c3 = 0
piece_on_c4 = 0
piece_on_c5 = 0
piece_on_c6 = 0
piece_on_c7 = 0
piece_on_c8 = 0
piece_on_d1 = 0
piece_on_d2 = 0
piece_on_d3 = 0
piece_on_d4 = 0
piece_on_d5 = 0
piece_on_d6 = 0
piece_on_d7 = 0
piece_on_d8 = 0
piece_on_e1 = 0
piece_on_e2 = 0
piece_on_e3 = 0
piece_on_e4 = 0
piece_on_e5 = 0
piece_on_e6 = 0
piece_on_e7 = 0
piece_on_e8 = 0
piece_on_f1 = 0
piece_on_f2 = 0
piece_on_f3 = 0
piece_on_f4 = 0
piece_on_f5 = 0
piece_on_f6 = 0
piece_on_f7 = 0
piece_on_f8 = 0
piece_on_g1 = 0
piece_on_g2 = 0
piece_on_g3 = 0
piece_on_g4 = 0
piece_on_g5 = 0
piece_on_g6 = 0
piece_on_g7 = 0
piece_on_g8 = 0
piece_on_h1 = 0
piece_on_h2 = 0
piece_on_h3 = 0
piece_on_h4 = 0
piece_on_h5 = 0
piece_on_h6 = 0
piece_on_h7 = 0
piece_on_h8 = 0

#Define piece attributes
pieces_fillcolor = "black"
pieces_pencolor = "black"
pieces_speed = 0

#Define variables containing the amounts of pieces
total_num_pieces = 32
num_white_pieces = 16
num_black_pieces = 16

##Define variables containing the amounts of pawns
total_num_pawns = 16
num_white_pawns = 8
num_black_pawns = 8

#Define variables containing the amounts of rooks
total_num_rooks = 4
num_white_rooks = 2
num_black_rooks = 2

#Define variables containing the amounts of knights
total_num_knights = 4
num_white_knights = 2
num_black_knights = 2

#Define variables containing the amounts of bishops
total_num_bishops = 4
num_white_bishops = 2
num_black_bishops = 2

#Define variables containing the amounts of queens
total_num_queens = 2
num_white_queens = 1
num_black_queens = 1

#Define variables containing the amounts of kings
total_num_kings = 2
num_white_kings = 1
num_black_kings = 1

#Define coordinates for each of the 64 squares
#Define a1's coordinates
a1_xcor = -260 + 0.5 * length_of_square
a1_ycor = -260 + 0.5 * length_of_square
a1_cors = a1_xcor, a1_ycor

#Define a2's coordinates
a2_xcor = a1_xcor + 0
a2_ycor = a1_ycor + length_of_square
a2_cors = a2_xcor, a2_ycor

#Define a3's coordinates
a3_xcor = a2_xcor + 0
a3_ycor = a2_ycor + length_of_square
a3_cors = a3_xcor, a3_ycor

#Define a4's coordinates
a4_xcor = a3_xcor + 0
a4_ycor = a3_ycor + length_of_square
a4_cors = a4_xcor, a4_ycor

#Define a5's coordinates
a5_xcor = a4_xcor + 0
a5_ycor = a4_ycor + length_of_square
a5_cors = a5_xcor, a5_ycor

#Define a6's coordinates
a6_xcor = a5_xcor + 0
a6_ycor = a5_ycor + length_of_square
a6_cors = a6_xcor, a6_ycor

#Define a7's coordinates
a7_xcor = a6_xcor + 0
a7_ycor = a6_ycor + length_of_square
a7_cors = a7_xcor, a7_ycor

#Define a8's coordinates
a8_xcor = a7_xcor + 0
a8_ycor = a7_ycor + length_of_square
a8_cors = a8_xcor, a8_ycor

#Define b1's coordinates
b1_xcor = a1_xcor + length_of_square
b1_ycor = a1_ycor + 0
b1_cors = b1_xcor, b1_ycor

#Define b2's coordinates
b2_xcor = b1_xcor + 0
b2_ycor = b1_ycor + length_of_square
b2_cors = b2_xcor, b2_ycor

#Define b3's coordinates
b3_xcor = b2_xcor + 0
b3_ycor = b2_ycor + length_of_square
b3_cors = b3_xcor, b3_ycor

#Define b4's coordinates
b4_xcor = b3_xcor + 0
b4_ycor = b3_ycor + length_of_square
b4_cors = b4_xcor, b4_ycor

#Define b5's coordinates
b5_xcor = b4_xcor + 0
b5_ycor = b4_ycor + length_of_square
b5_cors = b5_xcor, b5_ycor

#Define b6's coordinates
b6_xcor = b5_xcor + 0
b6_ycor = b5_ycor + length_of_square
b6_cors = b6_xcor, b6_ycor

#Define b7's coordinates
b7_xcor = b6_xcor + 0
b7_ycor = b6_ycor + length_of_square
b7_cors = b7_xcor, b7_ycor

#Define b8's coordinates
b8_xcor = b7_xcor + 0
b8_ycor = b7_ycor + length_of_square
b8_cors = b8_xcor, b8_ycor

#Define c1's coordinates
c1_xcor = b1_xcor + length_of_square
c1_ycor = b1_ycor + 0
c1_cors = c1_xcor, c1_ycor

#Define c2's coordinates
c2_xcor = c1_xcor + 0
c2_ycor = c1_ycor + length_of_square
c2_cors = c2_xcor, c2_ycor

#Define c3's coordinates
c3_xcor = c2_xcor + 0
c3_ycor = c2_ycor + length_of_square
c3_cors = c3_xcor, c3_ycor

#Define c4's coordinates
c4_xcor = c3_xcor + 0
c4_ycor = c3_ycor + length_of_square
c4_cors = c4_xcor, c4_ycor

#Define c5's coordinates
c5_xcor = c4_xcor + 0
c5_ycor = c4_ycor + length_of_square
c5_cors = c5_xcor, c5_ycor

#Define c6's coordinates
c6_xcor = c5_xcor + 0
c6_ycor = c5_ycor + length_of_square
c6_cors = c6_xcor, c6_ycor

#Define c7's coordinates
c7_xcor = c6_xcor + 0
c7_ycor = c6_ycor + length_of_square
c7_cors = c7_xcor, c7_ycor

#Define c8's coordinates
c8_xcor = c7_xcor + 0
c8_ycor = c7_ycor + length_of_square
c8_cors = c8_xcor, c8_ycor

#Define d1's coordinates
d1_xcor = c1_xcor + length_of_square
d1_ycor = c1_ycor + 0
d1_cors = d1_xcor, d1_ycor

#Define d2's coordinates
d2_xcor = d1_xcor + 0
d2_ycor = d1_ycor + length_of_square
d2_cors = d2_xcor, d2_ycor

#Define d3's coordinates
d3_xcor = d2_xcor + 0
d3_ycor = d2_ycor + length_of_square
d3_cors = d3_xcor, d3_ycor

#Define d4's coordinates
d4_xcor = d3_xcor + 0
d4_ycor = d3_ycor + length_of_square
d4_cors = d4_xcor, d4_ycor

#Define d5's coordinates
d5_xcor = d4_xcor + 0
d5_ycor = d4_ycor + length_of_square
d5_cors = d5_xcor, d5_ycor

#Define d6's coordinates
d6_xcor = d5_xcor + 0
d6_ycor = d5_ycor + length_of_square
d6_cors = d6_xcor, d6_ycor

#Define d7's coordinates
d7_xcor = d6_xcor + 0
d7_ycor = d6_ycor + length_of_square
d7_cors = d7_xcor, d7_ycor

#Define d8's coordinates
d8_xcor = d7_xcor + 0
d8_ycor = d7_ycor + length_of_square
d8_cors = d8_xcor, d8_ycor

#Define e1's coordinates
e1_xcor = d1_xcor + length_of_square
e1_ycor = d1_ycor + 0
e1_cors = e1_xcor, e1_ycor

#Define e2's coordinates
e2_xcor = e1_xcor + 0
e2_ycor = e1_ycor + length_of_square
e2_cors = e2_xcor, e2_ycor

#Define e3's coordinates
e3_xcor = e2_xcor + 0
e3_ycor = e2_ycor + length_of_square
e3_cors = e3_xcor, e3_ycor

#Define e4's coordinates
e4_xcor = e3_xcor + 0
e4_ycor = e3_ycor + length_of_square
e4_cors = e4_xcor, e4_ycor

#Define e5's coordinates
e5_xcor = e4_xcor + 0
e5_ycor = e4_ycor + length_of_square
e5_cors = e5_xcor, e5_ycor

#Define e6's coordinates
e6_xcor = e5_xcor + 0
e6_ycor = e5_ycor + length_of_square
e6_cors = e6_xcor, e6_ycor

#Define e7's coordinates
e7_xcor = e6_xcor + 0
e7_ycor = e6_ycor + length_of_square
e7_cors = e7_xcor, e7_ycor

#Define e8's coordinates
e8_xcor = e7_xcor + 0
e8_ycor = e7_ycor + length_of_square
e8_cors = e8_xcor, e8_ycor

#Define f1's coordinates
f1_xcor = e1_xcor + length_of_square
f1_ycor = e1_ycor + 0
f1_cors = f1_xcor, f1_ycor

#Define f2's coordinates
f2_xcor = f1_xcor + 0
f2_ycor = f1_ycor + length_of_square
f2_cors = f2_xcor, f2_ycor

#Define f3's coordinates
f3_xcor = f2_xcor + 0
f3_ycor = f2_ycor + length_of_square
f3_cors = f3_xcor, f3_ycor

#Define f4's coordinates
f4_xcor = f3_xcor + 0
f4_ycor = f3_ycor + length_of_square
f4_cors = f4_xcor, f4_ycor

#Define f5's coordinates
f5_xcor = f4_xcor + 0
f5_ycor = f4_ycor + length_of_square
f5_cors = f5_xcor, f5_ycor

#Define f6's coordinates
f6_xcor = f5_xcor + 0
f6_ycor = f5_ycor + length_of_square
f6_cors = f6_xcor, f6_ycor

#Define f7's coordinates
f7_xcor = f6_xcor + 0
f7_ycor = f6_ycor + length_of_square
f7_cors = f7_xcor, f7_ycor

#Define f8's coordinates
f8_xcor = f7_xcor + 0
f8_ycor = f7_ycor + length_of_square
f8_cors = f8_xcor, f8_ycor

#Define g1's coordinates
g1_xcor = f1_xcor + length_of_square
g1_ycor = f1_ycor + 0
g1_cors = g1_xcor, g1_ycor

#Define g2's coordinates
g2_xcor = g1_xcor + 0
g2_ycor = g1_ycor + length_of_square
g2_cors = g2_xcor, g2_ycor

#Define g3's coordinates
g3_xcor = g2_xcor + 0
g3_ycor = g2_ycor + length_of_square
g3_cors = g3_xcor, g3_ycor

#Define g4's coordinates
g4_xcor = g3_xcor + 0
g4_ycor = g3_ycor + length_of_square
g4_cors = g4_xcor, g4_ycor

#Define g5's coordinates
g5_xcor = g4_xcor + 0
g5_ycor = g4_ycor + length_of_square
g5_cors = g5_xcor, g5_ycor

#Define g6's coordinates
g6_xcor = g5_xcor + 0
g6_ycor = g5_ycor + length_of_square
g6_cors = g6_xcor, g6_ycor

#Define g7's coordinates
g7_xcor = g6_xcor + 0
g7_ycor = g6_ycor + length_of_square
g7_cors = g7_xcor, g7_ycor

#Define g8's coordinates
g8_xcor = g7_xcor + 0
g8_ycor = g7_ycor + length_of_square
g8_cors = g8_xcor, g8_ycor

#Define h1's coordinates
h1_xcor = g1_xcor + length_of_square
h1_ycor = g1_ycor + 0
h1_cors = h1_xcor, h1_ycor

#Define h2's coordinates
h2_xcor = h1_xcor + 0
h2_ycor = h1_ycor + length_of_square
h2_cors = h2_xcor, h2_ycor

#Define h3's coordinates
h3_xcor = h2_xcor + 0
h3_ycor = h2_ycor + length_of_square
h3_cors = h3_xcor, h3_ycor

#Define h4's coordinates
h4_xcor = h3_xcor + 0
h4_ycor = h3_ycor + length_of_square
h4_cors = h4_xcor, h4_ycor

#Define h5's coordinates
h5_xcor = h4_xcor + 0
h5_ycor = h4_ycor + length_of_square
h5_cors = h5_xcor, h5_ycor

#Define h6's coordinates
h6_xcor = h5_xcor + 0
h6_ycor = h5_ycor + length_of_square
h6_cors = h6_xcor, h6_ycor

#Define h7's coordinates
h7_xcor = h6_xcor + 0
h7_ycor = h6_ycor + length_of_square
h7_cors = h7_xcor, h7_ycor

#Define h8's coordinates
h8_xcor = h7_xcor + 0
h8_ycor = h7_ycor + length_of_square
h8_cors = h8_xcor, h8_ycor

#Define an empty list to store each of the chess piece turtles in
pieces_list = []

#####-Setup-#####
#Output a message for debugging if the user is in developer mode
if developer_mode == 1:
    print("Drawing the chessboard")

#Draw the full chessboard with labels
chessboard.draw_chessboard()

#Output a message for debugging if the user is in developer mode
if developer_mode == 1:
    print("Creating chess pieces")

#Create a turtle for each pawn and add it to the pieces master list
white_pawn_1 = trtl.Turtle()
white_pawn_1.shape(white_pawn_image)
white_pawn_1.hideturtle()
pieces_list.append(white_pawn_1)
white_pawn_2 = trtl.Turtle()
white_pawn_2.shape(white_pawn_image)
white_pawn_2.hideturtle()
pieces_list.append(white_pawn_2)
white_pawn_3 = trtl.Turtle()
white_pawn_3.shape(white_pawn_image)
white_pawn_3.hideturtle()
pieces_list.append(white_pawn_3)
white_pawn_4 = trtl.Turtle()
white_pawn_4.shape(white_pawn_image)
white_pawn_4.hideturtle()
pieces_list.append(white_pawn_4)
white_pawn_5 = trtl.Turtle()
white_pawn_5.shape(white_pawn_image)
white_pawn_5.hideturtle()
pieces_list.append(white_pawn_5)
white_pawn_6 = trtl.Turtle()
white_pawn_6.shape(white_pawn_image)
white_pawn_6.hideturtle()
pieces_list.append(white_pawn_6)
white_pawn_7 = trtl.Turtle()
white_pawn_7.shape(white_pawn_image)
white_pawn_7.hideturtle()
pieces_list.append(white_pawn_7)
white_pawn_8 = trtl.Turtle()
white_pawn_8.shape(white_pawn_image)
white_pawn_8.hideturtle()
pieces_list.append(white_pawn_8)
black_pawn_1 = trtl.Turtle()
black_pawn_1.shape(black_pawn_image)
black_pawn_1.hideturtle()
pieces_list.append(black_pawn_1)
black_pawn_2 = trtl.Turtle()
black_pawn_2.shape(black_pawn_image)
black_pawn_2.hideturtle()
pieces_list.append(black_pawn_2)
black_pawn_3 = trtl.Turtle()
black_pawn_3.shape(black_pawn_image)
black_pawn_3.hideturtle()
pieces_list.append(black_pawn_3)
black_pawn_4 = trtl.Turtle()
black_pawn_4.shape(black_pawn_image)
black_pawn_4.hideturtle()
pieces_list.append(black_pawn_4)
black_pawn_5 = trtl.Turtle()
black_pawn_5.shape(black_pawn_image)
black_pawn_5.hideturtle()
pieces_list.append(black_pawn_5)
black_pawn_6 = trtl.Turtle()
black_pawn_6.shape(black_pawn_image)
black_pawn_6.hideturtle()
pieces_list.append(black_pawn_6)
black_pawn_7 = trtl.Turtle()
black_pawn_7.shape(black_pawn_image)
black_pawn_7.hideturtle()
pieces_list.append(black_pawn_7)
black_pawn_8 = trtl.Turtle()
black_pawn_8.shape(black_pawn_image)
black_pawn_8.hideturtle()
pieces_list.append(black_pawn_8)

#Create a turtle for each rook and add it to the pieces master list
white_rook_1 = trtl.Turtle()
white_rook_1.shape(white_rook_image)
white_rook_1.hideturtle()
pieces_list.append(white_rook_1)
white_rook_2 = trtl.Turtle()
white_rook_2.shape(white_rook_image)
white_rook_2.hideturtle()
pieces_list.append(white_rook_2)
black_rook_1 = trtl.Turtle()
black_rook_1.shape(black_rook_image)
black_rook_1.hideturtle()
pieces_list.append(black_rook_1)
black_rook_2 = trtl.Turtle()
black_rook_2.shape(black_rook_image)
black_rook_2.hideturtle()
pieces_list.append(black_rook_2)

#Create a turtle for each knight and add it to the pieces master list
white_knight_1 = trtl.Turtle()
white_knight_1.shape(white_knight_image)
white_knight_1.hideturtle()
pieces_list.append(white_knight_1)
white_knight_2 = trtl.Turtle()
white_knight_2.shape(white_knight_image)
white_knight_2.hideturtle()
pieces_list.append(white_knight_2)
black_knight_1 = trtl.Turtle()
black_knight_1.shape(black_knight_image)
black_knight_1.hideturtle()
pieces_list.append(black_knight_1)
black_knight_2 = trtl.Turtle()
black_knight_2.shape(black_knight_image)
black_knight_2.hideturtle()
pieces_list.append(black_knight_2)

#Create a turtle for each bishop and add it to the pieces master list
white_bishop_1 = trtl.Turtle()
white_bishop_1.shape(white_bishop_image)
white_bishop_1.hideturtle()
pieces_list.append(white_bishop_1)
white_bishop_2 = trtl.Turtle()
white_bishop_2.shape(white_bishop_image)
white_bishop_2.hideturtle()
pieces_list.append(white_bishop_2)
black_bishop_1 = trtl.Turtle()
black_bishop_1.shape(black_bishop_image)
black_bishop_1.hideturtle()
pieces_list.append(black_bishop_1)
black_bishop_2 = trtl.Turtle()
black_bishop_2.shape(black_bishop_image)
black_bishop_2.hideturtle()
pieces_list.append(black_bishop_2)

#Create a turtle for the queens and add it to the pieces master list
white_queen = trtl.Turtle()
white_queen.shape(white_queen_image)
white_queen.hideturtle()
pieces_list.append(white_queen)
black_queen = trtl.Turtle()
black_queen.shape(black_queen_image)
black_queen.hideturtle()
pieces_list.append(black_queen)

#Create a turtle for the kings and add it to the pieces master list
white_king = trtl.Turtle()
white_king.shape(white_king_image)
white_king.hideturtle()
pieces_list.append(white_king)
black_king = trtl.Turtle()
black_king.shape(black_king_image)
black_king.hideturtle()
pieces_list.append(black_king)

#Output a message for debugging if the user is in developer mode
if developer_mode == 1:
    print("Setting piece properties")

#Set all pieces to a black fill color and prevent them from leaving tracers behind when they move or be visible as others are being created
for i in range(total_num_pieces):
    pieces_list[i].penup()
    pieces_list[i].fillcolor(pieces_fillcolor)
    pieces_list[i].pencolor(pieces_pencolor)
    pieces_list[i].speed(pieces_speed)

#Output a message for debugging if the user is in developer mode
if developer_mode == 1:
    print("Sending pieces to starting locations")

#Send white pawns to there starting location
#Update the tracker variables on their respective squares since they are now holding that piece
white_pawn_1.goto(a2_cors)
piece_on_a2 = white_pawn_1
white_pawn_2.goto(b2_cors)
piece_on_b2 = white_pawn_2
white_pawn_3.goto(c2_cors)
piece_on_c2 = white_pawn_3
white_pawn_4.goto(d2_cors)
piece_on_d2 = white_pawn_4
white_pawn_5.goto(e2_cors)
piece_on_e2 = white_pawn_5
white_pawn_6.goto(f2_cors)
piece_on_f2 = white_pawn_6
white_pawn_7.goto(g2_cors)
piece_on_g2 = white_pawn_7
white_pawn_8.goto(h2_cors)
piece_on_h2 = white_pawn_8

#Send black pawns to there starting location
#Update the tracker variables on their respective squares since they are now holding that piece
black_pawn_1.goto(a7_cors)
piece_on_a7 = black_pawn_1
black_pawn_2.goto(b7_cors)
piece_on_b7 = black_pawn_2
black_pawn_3.goto(c7_cors)
piece_on_c7 = black_pawn_3
black_pawn_4.goto(d7_cors)
piece_on_d7 = black_pawn_4
black_pawn_5.goto(e7_cors)
piece_on_e7 = black_pawn_5
black_pawn_6.goto(f7_cors)
piece_on_f7 = black_pawn_6
black_pawn_7.goto(g7_cors)
piece_on_g7 = black_pawn_7
black_pawn_8.goto(h7_cors)
piece_on_h7 = black_pawn_8

#Send white rooks to their starting location
#Update the tracker variables on their respective squares since they are now holding that piece
white_rook_1.goto(a1_cors)
piece_on_a1 = white_rook_1
white_rook_2.goto(h1_cors)
piece_on_h1 = white_rook_2

#Send black rooks to their starting location
#Update the tracker variables on their respective squares since they are now holding that piece
black_rook_1.goto(a8_cors)
piece_on_a8 = black_rook_1
black_rook_2.goto(h8_cors)
piece_on_h8 = black_rook_2

#Send white knights to their starting location
#Update the tracker variables on their respective squares since they are now holding that piece
white_knight_1.goto(b1_cors)
piece_on_b1 = white_knight_1
white_knight_2.goto(g1_cors)
piece_on_g1 = white_knight_2

#Send black knights to their starting location
#Update the tracker variables on their respective squares since they are now holding that piece
black_knight_1.goto(b8_cors)
piece_on_b8 = black_knight_1
black_knight_2.goto(g8_cors)
piece_on_g8 = black_knight_2

#Send white bishops to their starting location
#Update the tracker variables on their respective squares since they are now holding that piece
white_bishop_1.goto(c1_cors)
piece_on_c1 = white_bishop_1
white_bishop_2.goto(f1_cors)
piece_on_f1 = white_bishop_2

#Send black bishops to their starting location
#Update the tracker variables on their respective squares since they are now holding that piece
black_bishop_1.goto(c8_cors)
piece_on_c8 = black_bishop_1
black_bishop_2.goto(f8_cors)
piece_on_f8 = black_bishop_2

#Send queens to their starting location
#Update the tracker variables on their respective squares since they are now holding that piece
white_queen.goto(d1_cors)
piece_on_d1 = white_queen
black_queen.goto(d8_cors)
piece_on_d8 = black_queen

#Send kings to their starting location
#Update the tracker variables on their respective squares since they are now holding that piece
white_king.goto(e1_cors)
piece_on_e1 = white_king
black_king.goto(e8_cors)
piece_on_e8 = black_king

#Output a message for debugging if the user is in developer mode
if developer_mode == 1:
    print("Displaying pieces")

#For loop that shows the pieces after they have been moved
for i in range(total_num_pieces):
    pieces_list[i].showturtle()

#####-Game-#####


#####-Screen-#####
#Define a function that will execute code based on the keypress of a user
def a_pressed():
    if developer_mode == 1:
        print("A key pressed")

#Define a function that will execute code based on the keypress of a user
def b_pressed():
    if developer_mode == 1:
        print("B key pressed")

#Define a function that will execute code based on the keypress of a user
def c_pressed():
    if developer_mode == 1:
        print("C key pressed")

#Define a function that will execute code based on the keypress of a user
def d_pressed():
    if developer_mode == 1:
        print("D key pressed")

#Define a function that will execute code based on the keypress of a user
def e_pressed():
    if developer_mode == 1:
        print("E key pressed")

#Define a function that will execute code based on the keypress of a user
def f_pressed():
    if developer_mode == 1:
        print("F key pressed")

#Define a function that will execute code based on the keypress of a user
def g_pressed():
    if developer_mode == 1:
        print("G key pressed")

#Define a function that will execute code based on the keypress of a user
def h_pressed():
    if developer_mode == 1:
        print("H key pressed")

#Define a function that will execute code based on the keypress of a user
def i_pressed():
    if developer_mode == 1:
        print("I key pressed")

#Define a function that will execute code based on the keypress of a user
def j_pressed():
    if developer_mode == 1:
        print("J key pressed")

#Define a function that will execute code based on the keypress of a user
def k_pressed():
    if developer_mode == 1:
        print("K key pressed")

#Define a function that will execute code based on the keypress of a user
def l_pressed():
    if developer_mode == 1:
        print("L key pressed")

#Define a function that will execute code based on the keypress of a user
def m_pressed():
    if developer_mode == 1:
        print("M key pressed")

#Define a function that will execute code based on the keypress of a user
def n_pressed():
    if developer_mode == 1:
        print("N key pressed")

#Define a function that will execute code based on the keypress of a user
def o_pressed():
    if developer_mode == 1:
        print("O key pressed")

#Define a function that will execute code based on the keypress of a user
def p_pressed():
    if developer_mode == 1:
        print("P key pressed")

#Define a function that will execute code based on the keypress of a user
def q_pressed():
    if developer_mode == 1:
        print("Q key pressed")

#Define a function that will execute code based on the keypress of a user
def r_pressed():
    if developer_mode == 1:
        print("R key pressed")

#Define a function that will execute code based on the keypress of a user
def s_pressed():
    if developer_mode == 1:
        print("S key pressed")

#Define a function that will execute code based on the keypress of a user
def t_pressed():
    if developer_mode == 1:
        print("T key pressed")

#Define a function that will execute code based on the keypress of a user
def u_pressed():
    if developer_mode == 1:
        print("U key pressed")

#Define a function that will execute code based on the keypress of a user
def v_pressed():
    if developer_mode == 1:
        print("V key pressed")

#Define a function that will execute code based on the keypress of a user
def w_pressed():
    if developer_mode == 1:
        print("W key pressed")

#Define a function that will execute code based on the keypress of a user
def x_pressed():
    if developer_mode == 1:
        print("X key pressed")

#Define a function that will execute code based on the keypress of a user
def y_pressed():
    if developer_mode == 1:
        print("Y key pressed")

#Define a function that will execute code based on the keypress of a user
def z_pressed():
    if developer_mode == 1:
        print("Z key pressed")

#Define a function that will execute code based on the keypress of a user
def up_pressed():
    if developer_mode == 1:
        print("Up Arrow pressed")

#Define a function that will execute code based on the keypress of a user
def right_pressed():
    if developer_mode == 1:
        print("Right Arrow pressed")

#Define a function that will execute code based on the keypress of a user
def down_pressed():
    if developer_mode == 1:
        print("Down Arrow pressed")

#Define a function that will execute code based on the keypress of a user
def left_pressed():
    if developer_mode == 1:
        print("Left Arrow pressed")

#Call specific functions depending which key a user presses on their keyboard
wn.onkeypress(a_pressed, "a")
wn.onkeypress(b_pressed, "b")
wn.onkeypress(c_pressed, "c")
wn.onkeypress(d_pressed, "d")
wn.onkeypress(e_pressed, "e")
wn.onkeypress(f_pressed, "f")
wn.onkeypress(g_pressed, "g")
wn.onkeypress(h_pressed, "h")
wn.onkeypress(i_pressed, "i")
wn.onkeypress(j_pressed, "j")
wn.onkeypress(k_pressed, "k")
wn.onkeypress(l_pressed, "l")
wn.onkeypress(m_pressed, "m")
wn.onkeypress(n_pressed, "n")
wn.onkeypress(o_pressed, "o")
wn.onkeypress(p_pressed, "p")
wn.onkeypress(q_pressed, "q")
wn.onkeypress(r_pressed, "r")
wn.onkeypress(s_pressed, "s")
wn.onkeypress(t_pressed, "t")
wn.onkeypress(u_pressed, "u")
wn.onkeypress(v_pressed, "v")
wn.onkeypress(w_pressed, "w")
wn.onkeypress(x_pressed, "x")
wn.onkeypress(y_pressed, "y")
wn.onkeypress(z_pressed, "z")
wn.onkeypress(up_pressed, "Up")
wn.onkeypress(right_pressed, "Right")
wn.onkeypress(down_pressed, "Down")
wn.onkeypress(left_pressed, "Left")

#Listen for keypresses
wn.listen()

#Keep the display running and persistent
wn.mainloop()