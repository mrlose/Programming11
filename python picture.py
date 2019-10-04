import turtle
turtle.bgcolor("light blue")
turtle.pu()
turtle.setposition(-350,-150)
turtle.pd()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.setheading(0)
for i in range(2):
    turtle.forward(700)
    turtle.right(90)
    turtle.forward(700)
    turtle.right(90)
turtle.end_fill()

x=0
y=-50
def A (x,y,color1):
    turtle.pu()
    turtle.setposition(x,y)
    turtle.pd()
    turtle.fillcolor(color1)
    turtle.begin_fill()
    turtle.setheading(270)
    for i in range(10):
        turtle.right(100)
        turtle.forward(130)
        turtle.right(100)
    turtle.end_fill()
    turtle.pu()
    turtle.setposition(x-70,y-20)
    turtle.pd()
    turtle.pensize(5)
    turtle.setheading(270)
    turtle.forward(100)
    turtle.pensize(1)
A(x,y,"green")
A(200,-50,"red")
A(-200,-50,"orange")

x=100
y=150
def B (x,y):
    turtle.pu()
    turtle.setposition(x,y)
    turtle.pd()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    counter=0
    while counter<5:
        turtle.right(144.5)
        turtle.forward(100)
        counter=counter+1
    turtle.end_fill()
B(x,y)
B(-150,170)

x=100
y=100
def C (x,y):
    turtle.pu()
    turtle.setposition(x,y)
    turtle.pd()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.setheading(270)
    turtle.circle(20,180)
    turtle.setheading(270)
    turtle.circle(20,180)
    turtle.setheading(0)
    turtle.circle(20,180)
    turtle.setheading(90)
    turtle.circle(20,180)
    turtle.setheading(90)
    turtle.circle(20,180)
    turtle.setheading(180)
    turtle.circle(20,180)
    turtle.end_fill()
C(x,y)
C(-150,130)
C(210,210)

x=-300
y=210
def D (x,y):
    turtle.pu()
    turtle.setposition(x,y)
    turtle.pd()
    turtle.pensize(10)
    turtle.pencolor("white")
    turtle.setheading(90)
    turtle.circle(-40,180)
    turtle.setheading(270)
    turtle.circle(50,180)
D(x,y)
D(150,150)
