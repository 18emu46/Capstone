# Testing mouse aiming for Emu's game concept

# Import SPGL
import spgl
import math

# Create Classes
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)

	def motion(self, event):
		x1 = self.xcor()
		y1 = self.ycor()

		x2, y2 = event.x, event.y
		x2 -= 400
		y2 -= 300

		angle = math.atan2(y2 - y1, x2 - x1) * -180 / math.pi;
		self.setheading(angle)

class Ball(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 0
		self.state = "ready"
		
	def tick(self):
		if self.state == "firing":
			self.fd(self.speed)
		
			#Border checking
			if self.ycor() > 300:
				self.state = "ready"
				self.goto(player.xcor(), player.ycor())
			if self.ycor() < -300:
				self.state = "ready"
				self.goto(player.xcor(), player.ycor())
			if self.xcor() > 400:
				self.state = "ready"
				self.goto(player.xcor(), player.ycor())
			
					
	def shoot(self):
		if self.state == "ready":
			self.state = "firing"
			self.setheading(player.heading())
			self.speed = 10

class Obstacle(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.setheading(90)
		self.speed = 1
		
	def tick(self):
		self.fd(self.speed)
		
		# Border detection
		if self.ycor() > 290:
			self.sety(290)
			self.setheading(270)
		elif self.ycor() < -290:
			self.sety(-290)
			self.setheading(90)
			

# Create Functions


# Initial Game setup
game = spgl.Game(800, 600, "black", "Emu Test", 0)

# Create Sprites
player = Player("triangle", "white", -300, 0)
player.shapesize(1, 3, 0)

ball = Ball("circle", "white", -300, 0)

obstacle = Obstacle("square", "red", 0, 0)


# Create Labels

# Create Buttons

# Set mouse motion binding
canvas = spgl.turtle.getcanvas()
canvas.bind('<Motion>', player.motion)

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_SPACE, ball.shoot)

while True:
	# Call the game tick method
	game.tick()
