import turtle

def draw_square(some_turtle):
	fifteen_radius = 0
	complete_circle = 24
	while True:
		some_turtle.begin_fill()
		if fifteen_radius > complete_circle:
			some_turtle.end_fill()
		for i in range(1, 5):
			some_turtle.forward(100)
			some_turtle.right(90)	
		some_turtle.end_fill()
		some_turtle.right(15)
		fifteen_radius += 1
		if fifteen_radius > complete_circle * 2:
			break

def design_turtle():
	window = turtle.Screen()
	window.bgcolor("#8c66ff")
	leo = turtle.Turtle()
	leo.shape("circle")
	leo.color("blue", "cyan")
	leo.pencolor("#ff99cc")
	leo.pensize(3)
	leo.fillcolor("#b30059")
	leo.speed(25)
	leo.shapesize(3, 3)

	draw_square(leo)
	window.exitonclick()

design_turtle()