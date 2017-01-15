import pyglet

batch = pyglet.graphics.Batch()
PLAYER = 0
ENEMY = 1
ALIEN = 2
FRIENDLY = 3
POWERUP = 4

background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

class Vector(object):
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	def __add__(self, other):
		self.x += other.x
		self.y += other.y
		return self
class Entity(object):
	def __init__(self, image, affiliation, x = 0, y = 0, width = 0, height = 0):
		self.sprite = pyglet.sprite.Sprite(image, batch = batch, group = foreground)
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.velocity = Vector(0, 0)
		self.acceleration = Vector(0, 0)
		self.health = 1
		self.affiliation = affiliation
		self.iframes = 0
		self.delay = 0
		self.flip = False
	def overlaps(self, other):
		return (self.x < other.x + other.width and self.x + self.width > other.width and 
			self.y < other.y + other.height and self.y + self.height > other.y)
	def update(self, entities):
		self.velocity += self.acceleration
		self.x += self.velocity.x
		self.y += self.velocity.y
		self.sprite.x = self.x
		self.sprite.y = self.y
		if self.affiliation == PLAYER:
			for ent in entities:
				if ent.affiliation != PLAYER and ent.affiliation != FRIENDLY and (self.overlaps(ent)) and self.iframes <= 0:
					self.health -= 1	
					self.iframes = 60
					self.sprite.opacity = 128
			if self.iframes > 0:
				self.iframes -= 1
				if self.iframes == 0:
					self.sprite.opacity = 255
		elif self.affiliation == FRIENDLY:
			for ent in entities:
				if ent.affiliation != PLAYER and ent.affiliation != FRIENDLY and (self.overlaps(ent)):
					ent.health -= 1
					self.health = 0
		elif self.affiliation == ALIEN:
			if self.velocity.x == 0:
				self.velocity.x = 6
			if self.x < 64:
				self.velocity.x = 6
			elif self.x > 640 - 64:
				self.velocity.x = -6
			self.velocity.y = 2
		elif self.velocity.y == 0:
			self.velocity.y = 1

