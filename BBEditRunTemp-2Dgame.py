# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import random 
import math
import turtle

# Create Classes
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.lives = 5
		self.score = 0
		
	def rotate_up(self):
		self.left(10)
		
	def rotate_down(self):
		self.right(10)
		
class Ball(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.setheading(0)
		self.speed = 0
		
	def shoot(self):
		self.speed += 15

	def tick(self):
		self.fd(self.speed)
		
	def rotate_up(self):
		self.left(10)
		
	def rotate_down(self):
		self.right(10)
		


		
	
number = random.randint(1,9)

class Obstacle(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.setheading(90)
	
	def tick(self):
		global number
		self.fd(0)
		
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
ball = Ball("circle", "yellow", -470, 0)
obstacle = Obstacle("square", "red", 0, 0)
obstacle_2 = Obstacle("square", "red", 500, 0)
obstacle_3 = Obstacle("square", "red", 250, 0)
			
# Create Labels
label_score = spgl.Label("Score: 0", "white", -525, 270)  

label_lives = spgl.Label("Lives left: 5", "white", -525, 250)  


# Create Buttons

# Set Keyboard Bindings

game.set_keyboard_binding(ball.shoot, "Right")
game.set_keyboard_binding(player.rotate_up, "Up")
game.set_keyboard_binding(player.rotate_down, "Down")
game.set_keyboard_binding(ball.rotate_up, "Up")
game.set_keyboard_binding(ball.rotate_down, "Down")
while True:
    # Call the game tick method
	game.tick()
	
	if ball.xcor() > 530:
		player.score += 10
		ball.goto(-470, 0)
		ball.speed = 0
		label_score.update("Score: {}".format(player.score))

	if game.is_circle_collision(ball, obstacle, 20):
		player.lives -= 1 
		print("You lost a life")
		ball.goto(-470, 0)
		ball.speed = 0
		label_lives.update("Lives: {}".format(player.lives))
		
		
		
	if game.is_circle_collision(ball, obstacle_2, 20):
		player.lives -= 1 
		print("You lost a life")
		ball.goto(-470, 0)
		ball.speed = 0
		#play sound
		
	if game.is_circle_collision(ball, obstacle_3, 20):
		pass 
		
	
	
	
	# goal.move()

