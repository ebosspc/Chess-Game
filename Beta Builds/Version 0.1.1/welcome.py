#Define a function to welcome the user to the game
def welcome_user():
    #Create a message in the terminal instructing users how to use the program
    print("-----Welcome to the game!-----\nWould you like to read the instructions for the game?\n")

#Define a function to print the instructions for the game
def print_instructions():
    #Explain to users some basic info about the game
    print("\n-Game Info-")
    print("This game is a 2 player chess game with all of the rules of normal chess.")
    print("Be sure to find a partner to play with, as playing by yourself is rather boring.")

    #Explain the rules of the game, like how each piece moves
    print("\n-Rules-")
    print("Like with normal chess, there are 8 pawns, 2 rooks, 2 knights, 2 bishops, a queen, and a king on each side.")
    print("Each player has to pick one side: either white or black.")
    print("Each player is allowed 1 legal move per turn with any piece.")
    print("Pawns can only move forward 1 space, except if it is theirvery first move. If so, they can move forward 2 spaces.")
    print("It is important to note that when a pawn captures a piece, it can only do so by moving one square accross a diagonal.")
    print("The last exception/rule regarding pawns is the en-pessant rule.")
    print("If a player takes their aforementioned first move of 2 spaces,\nanother pawn can take that piece as if it only moved forward 1 square by capturing behind it.")
    print("Rooks can move upwards and accross the board and can take any piece along their path.")
    print("Knights can move in L-like shapes moving forward or back 2 squares, and then moving 1 square left or right, taking any piece in their path.")
    print("Bishops can move along diagonals, taking any piece in their path.")
    print("Queens are like a combination of rooks and bishops.\n They can move along any diagonal, horizontal, or vertical line, taking any piece in their path.")
    print("Kings can move 1 space in any direction of the 8 squares that incicle them.")
    
    #Describe the objective of the game
    print("\n-Objective-")
    print("When another piece threatents to take the king on its very next move, the king is put into check.")
    print("When the king is put in check, the player put in check must make a legal move to prevent their king from being taken.")
    print("If there are no legal moves a player can make, and the king is in check then the player is in checkmate and the other player wins!")
    print("Please note that in chess, a player can never be forced to make an illegal move,\nso if a player can't make a legal mvoe without putting their king into check, it is a stalemate and draw.")
    