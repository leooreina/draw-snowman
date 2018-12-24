# Draw a snowman while snowing in the background

import turtle

def draw_snowman(turtle_bryan):

	# drawing the circles
	turtle_bryan.begin_fill()
	turtle_bryan.circle(14)
	turtle_bryan.left(180)
	turtle_bryan.circle(30)
	turtle_bryan.left(90)
	turtle_bryan.end_fill()

	# pen stops drawing
	turtle_bryan.penup()

	turtle_bryan.forward(15)
	turtle_bryan.left(100)
	turtle_bryan.forward(10)

	# drawing the arms (1)
	turtle_bryan.pendown()
	turtle_bryan.forward(30)

	# pen stops drawing
	turtle_bryan.penup()

	turtle_bryan.right(180)
	turtle_bryan.forward(30)
	turtle_bryan.right(10)
	turtle_bryan.forward(20)
	turtle_bryan.right(10)

	# drawing the arms (2)
	turtle_bryan.pendown()
	turtle_bryan.forward(30)

	# pen stops drawing
	turtle_bryan.penup()

	turtle_bryan.right(100)
	turtle_bryan.forward(30)
	turtle_bryan.right(75)
	turtle_bryan.forward(20)


	# drawing the eyes (1)
	turtle_bryan.pendown()
	turtle_bryan.forward(3)

	# pen stops drawing
	turtle_bryan.penup()

	turtle_bryan.forward(5)
	turtle_bryan.left(15)

	# drawing the eyes (2)
	turtle_bryan.pendown()
	turtle_bryan.forward(3)

	# pen stops drawing
	turtle_bryan.penup()

	turtle_bryan.forward(90)
	turtle_bryan.right(178)
	turtle_bryan.forward(95)
	

	# drawing the noose (orange color)
	turtle_bryan.begin_fill()
	turtle_bryan.pendown()
	turtle_bryan.color("#e5a432")
	turtle_bryan.forward(20)
	turtle_bryan.left(165)
	turtle_bryan.forward(20)
	turtle_bryan.end_fill()

	turtle_bryan.penup()
	turtle_bryan.forward(60)
	turtle_bryan.right(172)
	turtle_bryan.forward(50)


	# drawing the scarf (red color)
	turtle_bryan.pendown()
	turtle_bryan.pensize(9)
	turtle_bryan.color("#aa1212")
	turtle_bryan.forward(18)
	turtle_bryan.left(175)
	turtle_bryan.forward(22)
	turtle_bryan.right(100)
	turtle_bryan.forward(8)
	turtle_bryan.left(20)
	turtle_bryan.forward(8)
	turtle_bryan.right(20)
	turtle_bryan.forward(8)

	turtle_bryan.penup()

	turtle_bryan.forward(60)

	turtle_bryan.pensize(2)
	turtle_bryan.color("#212020")

	turtle_bryan.left(100)
	turtle_bryan.forward(15)
	turtle_bryan.left(90)
	turtle_bryan.forward(105)
	turtle_bryan.left(90)

	# drawing the base of the hat
	turtle_bryan.begin_fill()
	turtle_bryan.pendown()
	turtle_bryan.forward(40)
	turtle_bryan.right(90)
	turtle_bryan.forward(5)
	turtle_bryan.right(90)
	turtle_bryan.forward(50)
	turtle_bryan.right(90)
	turtle_bryan.forward(5)
	turtle_bryan.right(90)
	turtle_bryan.forward(42)
	turtle_bryan.end_fill()

	turtle_bryan.penup()

	turtle_bryan.right(90)
	turtle_bryan.forward(5)

	# drawing the top of the hat
	turtle_bryan.color("#2d2c2c")
	turtle_bryan.begin_fill()
	turtle_bryan.pendown()
	turtle_bryan.forward(20)
	turtle_bryan.right(90)
	turtle_bryan.forward(35)
	turtle_bryan.right(90)
	turtle_bryan.forward(20)
	turtle_bryan.end_fill()

	turtle_bryan.penup()

	turtle_bryan.forward(100)

def aspects_turtle():
	window = turtle.Screen()
	window.bgcolor("#554ca3")
	bryan = turtle.Turtle()
	bryan.shape("turtle")
	bryan.shapesize(1, 1)
	bryan.pensize(2)
	bryan.speed(2)
	bryan.color("#3a3a3a", "#ffffff")

	draw_snowman(bryan)

	window.exitonclick()

aspects_turtle()