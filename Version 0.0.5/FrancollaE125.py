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
pawn_1 = trtl.Turtle()
pawn_1.append(pieces_list)
pawn_2 = trtl.Turtle()
pawn_2.append(pieces_list)
pawn_3 = trtl.Turtle()
pawn_3.append(pieces_list)
pawn_4 = trtl.Turtle()
pawn_4.append(pieces_list)
pawn_5 = trtl.Turtle()
pawn_5.append(pieces_list)
pawn_6 = trtl.Turtle()
pawn_6.append(pieces_list)
pawn_7 = trtl.Turtle()
pawn_7.append(pieces_list)
pawn_8 = trtl.Turtle()
pawn_8.append(pieces_list)

#Create a turtle for each rook and add it to the pieces master list
rook_1 = trtl.Turtle()
rook_1.append(pieces_list)
rook_2 = trtl.Turtle()
rook_2.append(pieces_list)

#Create a turtle for each knight and add it to the pieces master list
knight_1 = trtl.Turtle()
knight_1.append(pieces_list)
knight_2 = trtl.Turtle()
knight_2.append(pieces_list)

#Create a turtle for each bishop and add it to the pieces master list
bishop_1 = trtl.Turtle()
bishop_1.append(pieces_list)
bishop_2 = trtl.Turtle()
bishop_2.append(pieces_list)

#Create a turtle for the queen and add it to the pieces master list
queen = trtl.Turtle()
queen.append(pieces_list)

#Create a turtle forthe king and add it to the pieces master list
king = trtl.Turtle()
king.append(pieces_list)




#####-Game Config-#####


#####-Game-#####


#####-Screen-#####
#Generate a screen for the game to diplay on
wn = trtl.Screen()

#Keep the display running and persistent
wn.mainloop()