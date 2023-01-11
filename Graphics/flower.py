import turtle

##flower1
# tur = turtle.Turtle()
# tur.speed(20)
# tur.color("black", "orange")
# tur.begin_fill()
 
# for i in range(50):
#     tur.forward(300)
#     tur.left(170)
 
# tur.end_fill()
# turtle.done()

##flower2
# Set initial position
# turtle.penup ()
# turtle.left (90)
# turtle.fd (200)
# turtle.pendown ()
# turtle.right (90)

# # flower base
# turtle.fillcolor ("red")
# turtle.begin_fill ()
# turtle.circle (10,180)
# turtle.circle (25,110)
# turtle.left (50)
# turtle.circle (60,45)
# turtle.circle (20,170)
# turtle.right (24)
# turtle.fd (30)
# turtle.left (10)
# turtle.circle (30,110)
# turtle.fd (20)
# turtle.left (40)
# turtle.circle (90,70)
# turtle.circle (30,150)
# turtle.right (30)
# turtle.fd (15)
# turtle.circle (80,90)
# turtle.left (15)
# turtle.fd (45)
# turtle.right (165)
# turtle.fd (20)
# turtle.left (155)
# turtle.circle (150,80)
# turtle.left (50)
# turtle.circle (150,90)
# turtle.end_fill ()

# # Petal 1
# turtle.left (150)
# turtle.circle (-90,70)
# turtle.left (20)
# turtle.circle (75,105)
# turtle.setheading (60)
# turtle.circle (80,98)
# turtle.circle (-90,40)

# # Petal 2
# turtle.left (180)
# turtle.circle (90,40)
# turtle.circle (-80,98)
# turtle.setheading (-83)

# # Leaves 1
# turtle.fd (30)
# turtle.left (90)
# turtle.fd (25)
# turtle.left (45)
# turtle.fillcolor ("green")
# turtle.begin_fill ()
# turtle.circle (-80,90)
# turtle.right (90)
# turtle.circle (-80,90)
# turtle.end_fill ()
# turtle.right (135)
# turtle.fd (60)
# turtle.left (180)
# turtle.fd (85)
# turtle.left (90)
# turtle.fd (80)

# # Leaves 2
# turtle.right (90)
# turtle.right (45)
# turtle.fillcolor ("green")
# turtle.begin_fill ()
# turtle.circle (80,90)
# turtle.left (90)
# turtle.circle (80,90)
# turtle.end_fill ()
# turtle.left (135)
# turtle.fd (60)
# turtle.left (180)
# turtle.fd (60)
# turtle.right (90)
# turtle.circle (200,60)
# turtle.done()

##flower3
# import turtle
# import random
# import math

# def drawPolygon(myTurtle, sides, length):
#     angle = 360 / sides
#     for side in range(sides):
#         myTurtle.forward(length)
#         myTurtle.left(angle)

# def drawCircle(myTurtle, radius):
#     circumference = 2 * math.pi * radius
#     sides = 100
#     length = circumference / sides
#     drawPolygon(myTurtle, sides, length)

# def drawArc(myTurtle, radius, angle):
#     arc_length = 2 * math.pi * radius * angle / 360
#     sides = int(arc_length / 3) + 1
#     step_length = arc_length / sides
#     step_angle = angle / sides

#     for side in range(sides):
#         myTurtle.forward(step_length)
#         myTurtle.left(step_angle)

# def drawPetal(myTurtle, radius, angle):
#     drawArc(myTurtle, radius, angle)
#     myTurtle.left(180-angle)
#     drawArc(myTurtle, radius, angle)
#     myTurtle.left(180-angle)

# def drawFlower(myTurtle, petals, radius, angle):
#     for petal in range(petals):
#         drawPetal(myTurtle, radius, angle)
#         myTurtle.left( 360 / petals )

# def drawRandomFlower(myTurtle):
#     petals = random.randint(5, 10)
#     radius = random.randint(50, 150)
#     angle = random.randint(5, 72)
#     color = random.choice(['red', 'blue', 'green', 'black', 'orange'])

#     distance = random.randrange(250)
#     theta = random.randrange(359)

#     # Set new color
#     myTurtle.color(color)

#     # Move to random position
#     myTurtle.up()
#     myTurtle.left(theta)
#     myTurtle.forward(distance)

#     # Draw Random Flower
#     myTurtle.down()
#     drawFlower(myTurtle, petals, radius, angle)

#     # Go back to the home position.
#     myTurtle.up()
#     myTurtle.left(180)
#     myTurtle.forward(distance)

# window = turtle.Screen()
# george = turtle.Turtle()
# george.shape("turtle")
# george.speed(10000000000000000000000000000000000000000000000000**100000000000000000000000000000000000000000000000000000)

# for i in range(15):
#     drawRandomFlower(george)

from turtle import *
import turtle as tur

tur = tur.Turtle()
 

tur.penup ()
tur.left (90)
tur.fd (200)
tur.pendown ()
tur.right (90)
 

tur.fillcolor ("red")
tur.begin_fill ()
tur.circle (10,180)
tur.circle (25,110)
tur.left (50)
tur.circle (60,45)
tur.circle (20,170)
tur.right (24)
tur.fd (30)
tur.left (10)
tur.circle (30,110)
tur.fd (20)
tur.left (40)
tur.circle (90,70)
tur.circle (30,150)
tur.right (30)
tur.fd (15)
tur.circle (80,90)
tur.left (15)
tur.fd (45)
tur.right (165)
tur.fd (20)
tur.left (155)
tur.circle (150,80)
tur.left (50)
tur.circle (150,90)
tur.end_fill ()
 

tur.left (150)
tur.circle (-90,70)
tur.left (20)
tur.circle (75,105)
tur.setheading (60)
tur.circle (80,98)
tur.circle (-90,40)

tur.left (180)
tur.circle (90,40)
tur.circle (-80,98)
tur.setheading (-83)

tur.fd (30)
tur.left (90)
tur.fd (25)
tur.left (45)
tur.fillcolor ("dark green")
tur.begin_fill ()
tur.circle (-80,90)
tur.right (90)
tur.circle (-80,90)
tur.end_fill ()
tur.right (135)
tur.fd (60)
tur.left (180)
tur.fd (85)
tur.left (90)
tur.fd (80)
 
tur.right (90)
tur.right (45)
tur.fillcolor ("dark green")
tur.begin_fill ()
tur.circle (80,90)
tur.left (90)
tur.circle (80,90)
tur.end_fill ()
tur.left (135)
tur.fd (60)
tur.left (180)
tur.fd (60)
tur.right (90)
tur.circle (200,60)
tur.done()