'''
PLTW Lesson 1.2.5
@authors: Ethan Francolla
'''

#####-Imports-#####
#Import Turtle library for drawing and display functions
import turtle as trtl

#Import abstracted chessboard module for drawing a chessboard
import chessboard as chessboard


#####-Setup-#####
#Draw the full chessboard with labels
chessboard.draw_chessboard()

#Define an empty list to store each of the chess piece turtles in
pieces_list = []

#Create a turtle for each pawn and add it to the pieces master list
white_pawn_1 = trtl.Turtle()
white_pawn_1.append(pieces_list)
white_pawn_2 = trtl.Turtle()
white_pawn_2.append(pieces_list)
white_pawn_3 = trtl.Turtle()
white_pawn_3.append(pieces_list)
white_pawn_4 = trtl.Turtle()
white_pawn_4.append(pieces_list)
white_pawn_5 = trtl.Turtle()
white_pawn_5.append(pieces_list)
white_pawn_6 = trtl.Turtle()
white_pawn_6.append(pieces_list)
white_pawn_7 = trtl.Turtle()
white_pawn_7.append(pieces_list)
white_pawn_8 = trtl.Turtle()
white_pawn_8.append(pieces_list)
black_pawn_1 = trtl.Turtle()
black_pawn_1.append(pieces_list)
black_pawn_2 = trtl.Turtle()
black_pawn_2.append(pieces_list)
black_pawn_3 = trtl.Turtle()
black_pawn_3.append(pieces_list)
black_pawn_4 = trtl.Turtle()
black_pawn_4.append(pieces_list)
black_pawn_5 = trtl.Turtle()
black_pawn_5.append(pieces_list)
black_pawn_6 = trtl.Turtle()
black_pawn_6.append(pieces_list)
black_pawn_7 = trtl.Turtle()
black_pawn_7.append(pieces_list)
black_pawn_8 = trtl.Turtle()
black_pawn_8.append(pieces_list)

#Create a turtle for each rook and add it to the pieces master list
white_rook_1 = trtl.Turtle()
white_rook_1.append(pieces_list)
white_rook_2 = trtl.Turtle()
white_rook_2.append(pieces_list)
black_rook_1 = trtl.Turtle()
black_rook_1.append(pieces_list)
black_rook_2 = trtl.Turtle()
black_rook_2.append(pieces_list)

#Create a turtle for each knight and add it to the pieces master list
white_knight_1 = trtl.Turtle()
white_knight_1.append(pieces_list)
white_knight_2 = trtl.Turtle()
white_knight_2.append(pieces_list)
black_knight_1 = trtl.Turtle()
black_knight_1.append(pieces_list)
black_knight_2 = trtl.Turtle()
black_knight_2.append(pieces_list)

#Create a turtle for each bishop and add it to the pieces master list
white_bishop_1 = trtl.Turtle()
white_bishop_1.append(pieces_list)
white_bishop_2 = trtl.Turtle()
white_bishop_2.append(pieces_list)
black_bishop_1 = trtl.Turtle()
black_bishop_1.append(pieces_list)
black_bishop_2 = trtl.Turtle()
black_bishop_2.append(pieces_list)

#Create a turtle for the queens and add it to the pieces master list
white_queen = trtl.Turtle()
white_queen.append(pieces_list)
black_queen = trtl.Turtle()
black_queen.append(pieces_list)

#Create a turtle for the kings and add it to the pieces master list
white_king = trtl.Turtle()
white_king.append(pieces_list)
black_king = trtl.Turtle()
black_king.append(pieces_list)


#####-Game Config-#####


#####-Game-#####


#####-Screen-#####
#Generate a screen for the game to diplay on
wn = trtl.Screen()

#Keep the display running and persistent
wn.mainloop()