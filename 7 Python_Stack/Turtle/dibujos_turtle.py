import turtle
import  math


'''Agregando color al trazo'''
#turtle.color('blue')

'''Para dibujar una línea'''
#turtle.forward(100)

'''Para cambiar la dirección'''
#turtle.left(45)
#turtle.forward(100)

#turtle.right(45)
#turtle.forward(100)

#for i in range(10):
#    turtle.forward(100)
#    turtle.left(150)

#turtle.done()

def dibujarCuadrado(w,x,y,z):
    turtle.bgcolor(w)
    turtle.color(x,y)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(z)
        turtle.left(90)
    turtle.end_fill()
    turtle.done()

#dibujarCuadrado('yellow', 'red', 'orange', 200)

def dibujarCirculo(w,x,y,z):
    turtle.bgcolor(w)
    turtle.color(x,y)
    turtle.begin_fill()
    for i in range(1):
        turtle.circle(z)
    turtle.end_fill()
    turtle.done()

#dibujarCirculo('blue', 'white', 'turquoise', 120)    

def dibujarTriangulo(w,x,y,z):
    turtle.bgcolor(w)
    turtle.color(x,y)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(z)
        turtle.left(120)
    turtle.end_fill()
    turtle.done()

#dibujarTriangulo('pink','red', 'hotpink', 200)

def dibujarPuntoRadio(w,x,y):
    turtle.bgcolor(w)
    turtle.color(x)
    turtle.begin_fill()
    for i in range(1):
        turtle.forward(y)
    turtle.end_fill()
    turtle.done()

#dibujarPuntoRadio('black','white', 100)    

def dibujarRectangulo(w,x,y,z,a):
    turtle.bgcolor(w)
    turtle.color(x,y)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(z)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
    turtle.end_fill()
    turtle.done()

#dibujarRectangulo('black', 'white', 'yellow', 200, 60)

def dibujarHexagono(w,x,y,z,):
    turtle.bgcolor(w)
    turtle.color(x,y)
    turtle.begin_fill()
    for i in range(6):
        turtle.forward(z)
        turtle.left(60)
    turtle.end_fill()
    turtle.done()

#dibujarHexagono('black', 'white', 'purple', 150)    

def dibujarEstrellaNueve(w,x,y,z,):
    turtle.bgcolor(w)
    turtle.color(x,y)
    turtle.begin_fill()
    for i in range(9):
        turtle.forward(z)
        turtle.left(200)
    turtle.end_fill()
    turtle.done()

#dibujarEstrellaNueve('black', 'white', 'aqua', 200)    

def dibujarEstrellaCinco(w,x,y,z,):
    turtle.bgcolor(w)
    turtle.color(x,y)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(z)
        turtle.right(144)
    turtle.end_fill()
    turtle.done()

#dibujarEstrellaCinco('black', 'lightblue', 'white',  200)    

def dibujoJonathan():
    turtle.bgcolor("black")
    turtle.pensize(2)
    turtle.speed(0)

    for i in range(6):
        for colours in["red", "magenta","blue","cyan", "green", "yellow","white"] :
            turtle.color(colours)
            turtle.circle(100)
            turtle.left(10)
    turtle.hideturtle()
    turtle.done()

#dibujoJonathan()

def dibujoAndrea():
    turtle.bgcolor("black")
    colors = [ "red","purple","blue","green"]
    turtle.fillcolor("yellow")
    turtle.begin_fill() 
    for i in range(4):
        turtle.pencolor(colors[i % 4]) #cantidad de colores que toma por cada i
        turtle.width(5) #grosor
        turtle.forward(200) #dibujo
        turtle.left(90) #giro
    turtle.end_fill()
    turtle.exitonclick()

#dibujoAndrea()

from turtle import Turtle, Screen

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
turtle.hideturtle()

draw_flower(100,10, 'orange', 'yellow')
draw_flower(80,10, 'orange', 'red')
draw_flower(40,10, 'orange', 'yellow')

screen = Screen()
screen.exitonclick()

