# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import random 
import math
import turtle

game = spgl.Game(800, 600, "black", "splash.gif", 0)

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

	def motion(self, event):
		x1 = self.xcor()
		y1 = self.ycor()

		x2, y2 = event.x, event.y
		x2 -= 400
		y2 -= 300

		angle = math.atan2(y2 - y1, x2 - x1) * -180 / math.pi;
		self.setheading(angle)

		print(self.heading())
		
class Ball(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.setheading(0)
		self.speed = 20
		self.state = "ready"
		self.dx = 15
		self.dy = 0



	def shoot(self):
		self.state = "firing"
		# Calculate dx and dy
		angle = player.heading()
		self.dx = self.speed * math.cos((angle/180) * math.pi)
		self.dy = self.speed * math.sin((angle/180) * math.pi)	
		
		


	def tick(self):
		if self.state == "firing":
			self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
				

							
		

class Obstacle(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.setheading(90)
		self.speed = 7
		self.active = False
	
	def tick(self):
		if self.active == True:
			self.st()
			self.fd(self.speed)
		
			if self.xcor() > 530:
				self.setx(530)
				self.left(180)
			if self.xcor() < -530:
				self.setx(-530)
				self.left(180)
			if self.ycor() > 250:
				self.sety(250)
				self.left(180)
			if self.ycor() < -250:
				self.sety(-250)
				self.left(180)	

		else:
			self.ht()
	
		
# Create Functions
# Initial Game setup
game = spgl.Game(1100, 600, "black", "Uhhh Uhhh...Get It Across", 0)


 
# Create Sprites
player = Player("triangle", "white", -500, 0)
ball = Ball("circle", "yellow", -470, 0)
obstacle_1 = Obstacle("square", "red", 0, 300)
obstacle_2 = Obstacle("square", "red", 420, -300)
obstacle_3 = Obstacle("square", "red", 230, 0)
obstacle_4 = Obstacle("square", "red", 500, 124)			
# sprite_name.set_image("image_name.gif", width, height)
obstacle_1.set_image("brick.gif", 70, 100)
obstacle_2.set_image("brick.gif", 70, 100)
obstacle_3.set_image("brick.gif", 70, 100)
ball.set_image("ball.gif", 0.99, 0.99)
#player.set_image("MainGuySpriteSheet.gif", 65, 65)





obstacles = [obstacle_1, obstacle_2, obstacle_3]

obstacle_1.active = True

# Create Labels
label_score = spgl.Label("Score: 0", "white", -525, 270)

label_lives = spgl.Label("Lives left: 5", "white", -525, 250)  


# Create Buttons

# Set Keyboard Bindings

game.set_keyboard_binding(ball.shoot, "Right")

	
# Set mouse motion binding
canvas = spgl.turtle.getcanvas()
canvas.bind('<Motion>', player.motion)

while True:
	
	if player.score == 40:
		for obstacle in obstacles:
			obstacle.speed += 5
		player.score += 10
		
	if player.score >= 20:
		obstacle_3.active = True
		
	if player.score == 50:
		for obstacle in obstacles:
			obstacle.speed += 3
		player.score += 10
	
	if player.score >= 50:
		obstacle_2.active = True
	
	if player.score == 70:
		for obstacle in obstacles:
			obstacle.speed += 8	
		
		player.score += 10
		
	if player.score == 100:
		pass
		
	
    # Call the game tick method
	game.tick()
	
	
	if player.score < 70:
		if ball.xcor() > 530:
			player.score += 10
			ball.goto(-470, 0)
			ball.state = "ready"
			label_score.update("Score: {}".format(player.score))
	if player.score >= 70:
		if ball.xcor() > 630:
			player.score += 10
			ball.goto(-470, 0)
			ball.state = "ready"
			label_score.update("Score: {}".format(player.score))



	for obstacle in obstacles:
		if game.is_collision(ball, obstacle) and obstacle.active == True:
			player.lives -= 1 
			print("You lost a life")
			ball.goto(-470, 0)
			ball.state = "ready"
			label_lives.update("Lives: {}".format(player.lives))

	if player.lives <= -1:
		break 
  
		

		
	
	
	
	# goal.move()

