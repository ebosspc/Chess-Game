import turtle as trtl

e5_xcor = 0
e5_ycor = 0
e5_cors = e5_xcor, e5_ycor

a1_xcor = -100
a1_ycor = -100
a1_cors = a1_xcor, a1_ycor

test_turtle = trtl.Turtle()
test_turtle.goto(e5_cors)

piece_on_e5 = 1
piece_on_a1 = 0


initial_input = input("On which square do you want to move a piece from?: ")
if initial_input == "e5":
    if piece_on_e5 == 1:
        other_input = input("where do you want to move the piece to?: ")
        if other_input == "a1":
            test_turtle.goto(a1_cors)
            piece_on_a1 = 1

wn = trtl.Screen()
wn.mainloop()
