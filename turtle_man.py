import turtle
import random

drawer = turtle.Turtle()
drawer.hideturtle()

franklin = turtle.Turtle()

#Set turtle's initial shape to a turtle
franklin.shape("turtle")

#Get the screen object
screen = turtle.Screen()

point_list = []
DOT_RADIUS = 3
range_x = (0,300)
range_y = (0, 300)

def move_turtle_to(position):
    drawer.up()
    drawer.goto(position[0], position[1])
    drawer.down()

def draw_dot(radius=DOT_RADIUS):
    drawer.dot(DOT_RADIUS)

for _ in range(10):
    x_coor = random.randrange(*range_x)
    y_coor = random.randrange(*range_y)
    point_list.append((x_coor,y_coor))

print "point_list:", point_list

for point in point_list:
    move_turtle_to(point)
    draw_dot(point)

#mainloop
turtle.mainloop()
