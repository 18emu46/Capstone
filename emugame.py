# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import random 
import tkinter 
from tkinter import messagebox



# Create Classes
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		score = 0


number = random.randint(1,9)

class Obstacle(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.setheading(90)
	
	def tick(self):
		
		global number
		self.fd(number)
		
		 
		if self.xcor() > 530:
			self.setx(530)
			self.left(180)
		if self.xcor() < -530:
			self.setx(-530)
			self.left(180)
		if self.ycor() > 290:
			self.sety(290)
			self.left(180)
		if self.ycor() < -290:
			self.sety(-290)
			self.left(180)	
			
# Create Functions
# Initial Game setup
game = spgl.Game(1100, 600, "black", "Uhhh Uhhh...Get It Across", 0)



 
# Create Sprites
player = Player("triangle", "white", -500, 0)
ball = Player("circle", "yellow", -470, 0)
obstacle = Obstacle("square", "red", 0, 0)
obstacle_2 = Obstacle("square", "red", 500, 0)

# Create Labels


# Create Buttons

# Set Keyboard Bindings

while True:
    # Call the game tick method
	game.tick()
	player.move()
	# goal.move()

