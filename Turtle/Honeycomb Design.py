import turtle
import random

#Variables
length = (30)
hexturn = (60)
move = (length*1.75)
turn = (90)
notimes = (2)
ccham = turtle.Turtle()

#Functions
def getRGB(ccham):
	turtle.colormode(255)
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	ccham.color(r,g,b)

def shape(ccham):
	getRGB(ccham)
	ccham.begin_fill()
	for i in range(6):
		ccham.forward(length)
		ccham.right(hexturn)
	ccham.end_fill()

def outline(ccham):
	ccham.color('#ffffff')
	for i in range(6):
		ccham.forward(length)
		ccham.right(hexturn)

def next(ccham):
	ccham.pu()
	ccham.right(turn)
	ccham.forward(move)
	ccham.left(turn)
	ccham.pd()

def nextrow(ccham):
	ccham.pu()
	ccham.left(turn)
	ccham.forward(move*3)
	ccham.left(30)
	ccham.forward(length)
	ccham.left(hexturn)
	ccham.forward(length*1.1)
	ccham.right(180)
	ccham.pd()

def startpoint(ccham):
	ccham.pu()
	ccham.setx(-60)
	ccham.sety(-60)
	ccham.forward(136)
	ccham.left(turn)
	ccham.forward(80)
	ccham.right(turn)
	ccham.pd()

def square(ccham):
	ccham.pu()
	ccham.setx(-300)
	ccham.sety(-300)
	ccham.pd()
	getRGB(ccham)
	ccham.begin_fill()
	for i in range(4):
		ccham.forward(600)
		ccham.right(turn)
	ccham.end_fill()

def end(ccham):
	ccham.pu()
	ccham.setx(-300)
	ccham.sety(-300)
	ccham.pd()

ccham.shape("circle")
ccham.left(turn)
square(ccham)
startpoint(ccham)
for i in range(4):
	for i in range(4):
		shape(ccham)
		outline(ccham)
		next(ccham)
	nextrow(ccham)
end(ccham)

turtle.done()