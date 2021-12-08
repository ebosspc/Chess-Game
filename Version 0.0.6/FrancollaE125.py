'''
PLTW Lesson 1.2.5
@authors: Ethan Francolla
'''

#####-Imports-#####
#Import Turtle library for drawing and display functions
import turtle as trtl

#Import abstracted chessboard module for drawing a chessboard
import chessboard as chessboard


#####-Game Config-#####
#Define the chess board's initial attributes
number_of_sides = 4
number_of_squares = 64
number_of_squares_on_side = number_of_squares / 8
length_of_side = 520
length_of_square = length_of_side / 8

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
a1_xcor = -100
a1_ycor = -100
a1_cors = a1_xcor, a1_ycor

#Define a2's coordinates
a2_xcor = a1_xcor + length_of_square
a2_ycor = a1_ycor + 0
a2_cors = a2_xcor, a2_ycor

#Define a3's coordinates
a3_xcor = a2_xcor + length_of_square
a3_ycor = a2_ycor + 0
a3_cors = a3_xcor, a3_ycor

#Define a4's coordinates
a4_xcor = a3_xcor + length_of_square
a4_ycor = a3_ycor + 0
a4_cors = a4_xcor, a4_ycor

#Define a5's coordinates
a5_xcor = a4_xcor + length_of_square
a5_ycor = a4_ycor + 0
a5_cors = a5_xcor, a5_ycor

#Define a6's coordinates
a6_xcor = a5_xcor + length_of_square
a6_ycor = a5_ycor + 0
a6_cors = a6_xcor, a6_ycor

#Define a7's coordinates
a7_xcor = a6_xcor + length_of_square
a7_ycor = a6_ycor + 0
a7_cors = a7_xcor, a7_ycor

#Define a8's coordinates
a8_xcor = a7_xcor + length_of_square
a8_ycor = a7_ycor + 0
a8_cors = a8_xcor, a8_ycor

#Define b1's coordinates
b1_xcor = a1_xcor + 0
b1_ycor = a1_ycor + length_of_square
b1_cors = b1_xcor, b1_ycor

#Define b2's coordinates
b2_xcor = b1_xcor + length_of_square
b2_ycor = b1_ycor + 0
b2_cors = b2_xcor, b2_ycor

#Define b3's coordinates
b3_xcor = b2_xcor + length_of_square
b3_ycor = b2_ycor + 0
b3_cors = b3_xcor, b3_ycor

#Define b4's coordinates
b4_xcor = b3_xcor + length_of_square
b4_ycor = b3_ycor + 0
b4_cors = b4_xcor, b4_ycor

#Define b5's coordinates
b5_xcor = b4_xcor + length_of_square
b5_ycor = b4_ycor + 0
b5_cors = b5_xcor, b5_ycor

#Define b6's coordinates
b6_xcor = b5_xcor + length_of_square
b6_ycor = b5_ycor + 0
b6_cors = b6_xcor, b6_ycor

#Define b7's coordinates
b7_xcor = b6_xcor + length_of_square
b7_ycor = b6_ycor + 0
b7_cors = b7_xcor, b7_ycor

#Define b8's coordinates
b8_xcor = b7_xcor + length_of_square
b8_ycor = b7_ycor + 0
b8_cors = b8_xcor, b8_ycor

#Define an empty list to store each of the chess piece turtles in
pieces_list = []

#####-Setup-#####
#Draw the full chessboard with labels
chessboard.draw_chessboard()

#Create a turtle for each pawn and add it to the pieces master list
white_pawn_1 = trtl.Turtle()
pieces_list.append(white_pawn_1)
white_pawn_2 = trtl.Turtle()
pieces_list.append(white_pawn_2)
white_pawn_3 = trtl.Turtle()
pieces_list.append(white_pawn_3)
white_pawn_4 = trtl.Turtle()
pieces_list.append(white_pawn_4)
white_pawn_5 = trtl.Turtle()
pieces_list.append(white_pawn_5)
white_pawn_6 = trtl.Turtle()
pieces_list.append(white_pawn_6)
white_pawn_7 = trtl.Turtle()
pieces_list.append(white_pawn_7)
white_pawn_8 = trtl.Turtle()
pieces_list.append(white_pawn_8)
black_pawn_1 = trtl.Turtle()
pieces_list.append(black_pawn_1)
black_pawn_2 = trtl.Turtle()
pieces_list.append(black_pawn_2)
black_pawn_3 = trtl.Turtle()
pieces_list.append(black_pawn_3)
black_pawn_4 = trtl.Turtle()
pieces_list.append(black_pawn_4)
black_pawn_5 = trtl.Turtle()
pieces_list.append(black_pawn_5)
black_pawn_6 = trtl.Turtle()
pieces_list.append(black_pawn_6)
black_pawn_7 = trtl.Turtle()
pieces_list.append(black_pawn_7)
black_pawn_8 = trtl.Turtle()
pieces_list.append(black_pawn_8)

#Create a turtle for each rook and add it to the pieces master list
white_rook_1 = trtl.Turtle()
pieces_list.append(white_rook_1)
white_rook_2 = trtl.Turtle()
pieces_list.append(white_rook_2)
black_rook_1 = trtl.Turtle()
pieces_list.append(black_rook_1)
black_rook_2 = trtl.Turtle()
pieces_list.append(black_rook_2)

#Create a turtle for each knight and add it to the pieces master list
white_knight_1 = trtl.Turtle()
pieces_list.append(white_knight_1)
white_knight_2 = trtl.Turtle()
pieces_list.append(white_knight_2)
black_knight_1 = trtl.Turtle()
pieces_list.append(black_knight_1)
black_knight_2 = trtl.Turtle()
pieces_list.append(black_knight_2)

#Create a turtle for each bishop and add it to the pieces master list
white_bishop_1 = trtl.Turtle()
pieces_list.append(white_bishop_1)
white_bishop_2 = trtl.Turtle()
pieces_list.append(white_bishop_2)
black_bishop_1 = trtl.Turtle()
pieces_list.append(black_bishop_1)
black_bishop_2 = trtl.Turtle()
pieces_list.append(black_bishop_2)

#Create a turtle for the queens and add it to the pieces master list
white_queen = trtl.Turtle()
pieces_list.append(white_queen)
black_queen = trtl.Turtle()
pieces_list.append(black_queen)

#Create a turtle for the kings and add it to the pieces master list
white_king = trtl.Turtle()
pieces_list.append(white_king)
black_king = trtl.Turtle()
pieces_list.append(black_king)

#Set all pieces to a black fill color and prevent them from leaving tracers behind when they move
for i in range(total_num_pieces):
    pieces_list[i].penup()
    pieces_list[i].fillcolor(pieces_fillcolor)
    pieces_list[i].pencolor(pieces_pencolor)
    pieces_list[i].speed(pieces_speed)


#####-Game-#####


#####-Screen-#####
#Generate a screen for the game to diplay on
wn = trtl.Screen()

#Keep the display running and persistent
wn.mainloop()