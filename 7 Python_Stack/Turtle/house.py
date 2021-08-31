import turtle
from turtle import Turtle, Screen

turtle.speed(0)

#Grass
#sturtle.bgcolor('green')
turtle.penup()
turtle.goto(-400, -400)
turtle.pendown()
def dibujarRectangulo(x,y,z,a):
    turtle.color(x, y)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(z)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
    turtle.end_fill()
    #turtle.done()
dibujarRectangulo('green', 'green', 800, 300)

#Sky
turtle.penup()
turtle.goto(-400, -100)
turtle.pendown()

dibujarRectangulo('deepskyblue', 'deepskyblue', 800, 500)

#Sun
turtle.penup()
turtle.goto(-290, 210)
turtle.pendown()

def dibujarCirculo(y,z):
    turtle.color(y)
    turtle.begin_fill()
    for i in range(1):
        turtle.circle(z)
    turtle.end_fill()
    #turtle.done()
dibujarCirculo('yellow', 35) 

#Cloud
turtle.penup()
turtle.goto(200, 200)
turtle.pendown()
dibujarCirculo('white', 25) 

turtle.penup()
turtle.goto(230, 180)
turtle.pendown()
dibujarCirculo('white', 25) 

turtle.penup()
turtle.goto(240, 210)
turtle.pendown()
dibujarCirculo('white', 25) 

turtle.penup()
turtle.goto(270, 190)
turtle.pendown()
dibujarCirculo('white', 25) 

#House
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
turtle.pensize(3)

def dibujarCuadrado(x,y,z):
    turtle.color(x,y)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(z)
        turtle.left(90)
    turtle.end_fill()
    #turtle.done()
dibujarCuadrado('chocolate', 'orange', 170)

#Chimney
turtle.penup()
turtle.goto(20, 130)
turtle.pendown()
dibujarRectangulo('brown', 'brown', 40,100)

#Roof
turtle.penup()
turtle.goto(-127, 70)
turtle.pendown()

def dibujarTriangulo(y,z):
    turtle.color(y)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(z)
        turtle.left(120)
    turtle.end_fill()
    #turtle.done()
dibujarTriangulo('brown', 225)

#Window 1
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
dibujarCuadrado('black', 'aqua', 50)

#Window 1 Cross - Horizontal Line
turtle.penup()
turtle.goto(0, 25)
turtle.pendown()

def dibujarPuntoRadio(x,y):
    turtle.color(x)
    turtle.begin_fill()
    for i in range(1):
        turtle.forward(y)
    turtle.end_fill()
    #turtle.done()
dibujarPuntoRadio('black', 50)    

#Window 1 Cross - Vertical Line
turtle.penup()
turtle.goto(25, 0)
turtle.pendown()
turtle.left(90)
dibujarPuntoRadio('black', 50)    

#Window 2
turtle.penup()
turtle.goto(-80, 0)
turtle.pendown()
turtle.right(90)
dibujarCuadrado('black', 'aqua', 50)

#Window 2 Cross - Horizontal Line
turtle.penup()
turtle.goto(-80, 25)
turtle.pendown()
dibujarPuntoRadio('black', 50)    

#Window 2 Cross - Vertical Line
turtle.penup()
turtle.goto(-55, 0)
turtle.pendown()
turtle.left(90)
dibujarPuntoRadio('black', 50)    

#Door
turtle.penup()
turtle.goto(-40, -97)
turtle.pendown()
turtle.right(90)
dibujarRectangulo('darkred', 'red', 50, 80)

#Door Handle
turtle.penup()
turtle.goto(0, -60)
turtle.pendown()
dibujarCirculo('black', 4)

#Flower
def draw_petal(turtle, radius):
    heading = turtle.heading()
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.setheading(heading)

def draw_flower(radio, petalos, color_line, color_fill):
    turtle.begin_fill()
    for _ in range(petalos):
            turtle.color(color_line, color_fill )
            draw_petal(turtle, radio)
            turtle.left(360 / petalos)
    turtle.end_fill()

#tallo y hoja
turtle.penup()
turtle.goto(240, -100)
turtle.pendown()
dibujarRectangulo('darkgreen', 'green', 1, 30)
turtle.penup()
turtle.goto(240, -90)
turtle.pendown()
draw_flower(8, 2, 'darkgreen', 'green')

turtle.penup()
turtle.goto(190, -100)
turtle.pendown()
dibujarRectangulo('darkgreen', 'green', 1, 30)
turtle.penup()
turtle.goto(190, -90)
turtle.pendown()
draw_flower(8, 2, 'darkgreen', 'green')


#Pétalos
turtle.penup()
turtle.goto(240, -70)
turtle.pensize(1)
turtle.pendown()
draw_flower(20,8, 'orange', 'yellow')
turtle.penup()
turtle.goto(190, -70)
turtle.pensize(1)
turtle.pendown()
draw_flower(20,10, 'orange', 'red')



screen = Screen()


turtle.hideturtle()
turtle.done()   


