import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

jt = turtle.Turtle()
jt.color("blue")

size = [20, 40, 60, 80, 100]

for x in size:
    drawSquare(jt, x)
    jt.penup()
    jt.backward(10)
    jt.right(90)
    jt.forward(10)
    jt.left(90)
    jt.pendown()
        

wn.exitonclick()
