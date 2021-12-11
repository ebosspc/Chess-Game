import turtle as trtl
wn = trtl.Screen()

number_of_sides = 4
number_of_squares = 64
number_of_squares_on_side = number_of_squares / 8
length_of_side = 520
length_of_square = length_of_side / 8

a1_xcor = -260 + 0.5 * length_of_square
a1_ycor = -260 + 0.5 * length_of_square
a1_cors = a1_xcor, a1_ycor

#Define a2's coordinates
a2_xcor = a1_xcor + 0
a2_ycor = a1_ycor + length_of_square
a2_cors = a2_xcor, a2_ycor

test_turtle = trtl.Turtle()
test_turtle.goto(a1_cors)
test_turtle_2 = trtl.Turtle()
test_turtle_2.goto(a2_cors)

bishop_image = "black_bishop.gif"
wn.addshape(bishop_image)
test_turtle.shape(bishop_image)

piece_on_a1 = test_turtle
piece_on_a2 = test_turtle_2


possible_squares_list = ["a1","a2","a3","a4","a5","a6","a7","a8","b1","b2","b3","b4","b5","b6","b7","b8",
"c1","c2","c3","c4","c5","c6","c7","c8","d1","d2","d3","d4","d5","d6","d7","d8",
"e1","e2","e3","e4","e5","e6","e7","e8","f1","f2","f3","f4","f5","f6","f7","f8",
"g1","g2","g3","g4","g5","g6","g7","g8","h1","h2","h3","h4","h5","h6","h7","h8"]

while (True):
    global moving_piece
    initial_input = input("On which square is the piece you want to move?: ")
    while initial_input not in possible_squares_list:
        initial_input = input("On which square is the piece you want to move?: ")
    if initial_input == "a1":
        moving_piece = piece_on_a1
        piece_on_a1 = 0
    if initial_input == "a2":
        moving_piece = piece_on_a2
        piece_on_a2 = 0

    other_input = input("Where do you want to move the piece to?: ")
    while other_input not in possible_squares_list:
        other_input = input("Where do you want to move the piece to?: ")
    if other_input == "a1":
        if piece_on_a1 != 0:
            piece_on_a1.clear()
            piece_on_a1.hideturtle()
            piece_on_a1 = 0
        moving_piece.goto(a1_cors)
        piece_on_a1 = moving_piece
    if other_input =="a2":
        if piece_on_a2 != 0:
            piece_on_a2.clear()
            piece_on_a2.hideturtle()
            piece_on_a2 = 0
        moving_piece.goto(a2_cors)
        piece_on_a2 = moving_piece





'''

while initial_input not in possible_squares_list:
    if initial_input == "a1":
        other_input = input("where do you want to move the piece to?: ")
        while other_input not in possible_squares_list[]:



        if other_input == "a2":
            test_turtle.goto(a1_cors)
            piece_on_a1 = 1


'''



wn.mainloop()
