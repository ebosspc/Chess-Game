import turtle as trtl

writer = trtl.Turtle()
writer.penup()

writer.write("A", align = "center", font = ("Times New Roman", 20, "normal"))

writer.forward(50)

writer.write("B", align = "center", font = ("Times New Roman", 20, "normal"))

wn = trtl.Screen()

wn.mainloop()