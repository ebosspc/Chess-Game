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

pieces_fillcolor = "black"
pieces_pencolor = "black"
pieces_speed = 0

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