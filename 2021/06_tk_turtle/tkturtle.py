from tkinter import *
import turtle

window = Tk()
canvas = Canvas(master=window, width=500, height=500)
canvas.pack()

t = turtle.RawTurtle(canvas)


def draw_turtle():
    length = 100

    while length > 0:
        t.forward(length)
        t.left(90)
        length -= 5

    t.penup()
    t.goto(200, 100)
    t.pendown()
    t.begin_fill()
    t.fillcolor("red")
    t.circle(50)
    t.end_fill()


button = Button(window, text="클릭하세요", command=draw_turtle)
button.pack()

window.mainloop()
