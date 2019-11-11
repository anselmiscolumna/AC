# Import libraries
from graphics import *
import time 

#Setup the graphics maze
win =  GraphWin("Dungeon Map", 600, 600)
win.setBackground("black")

#Dimensions of the blocks used for the maze walls

#Function for printing the walls
def wall(x1, y1, x2, y2):
	pt1 = Point(x1, y1)
	pt2 = Point(x2, y2)
	wall = Rectangle(pt1, pt2)
	wall.setFill("white")
	wall.draw(win)

#Function for the player's position
def player():
	position = Circle(Point())
#Walls built
#Maze Outline
for i in range(22):
	x = i * 25
	wall(25 + x, 25 , 50 + x, 50)

for i in range(22):
	x = i * 25
	wall(25, 25 + x, 50, 50 + x)

for i in range(22):
	x = i * 25
	wall(550, 25 + x , 575, 50 + x)

for i in range(22):
	x = i * 25
	wall(25 + x, 550, 50 + x, 575)

#First Path

for i in range(22):
	x = i * 25
	wall(25 + x, 25 , 50 + x, 50)








wall(25, 50, 50, 75)

wall(25, 50, 50, 75)
wall(25, 75, 50, 100)
wall(25, 100, 50, 125)
wall(50, 100, 75, 125)
wall(75, 100, 100, 125)


mazeOutline = Rectangle(Point(25, 25), Point(575, 575))
mazeOutline.setOutline("white")
mazeOutline.draw(win)



win.getKey()

