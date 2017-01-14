import pyglet

batch = pyglet.graphics.Batch()
PLAYER = 0
ENEMY = 1

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
		self.sprite = pyglet.sprite.Sprite(image, batch = batch)
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.velocity = Vector(0, 0)
		self.acceleration = Vector(0, 0)
		self.health = 1
		self.affiliation = affiliation
	def overlaps(self, other):
		return (self.x < other.x + other.width and self.x + self.width > other.width and 
			self.y < other.y + other.height and self.y + self.height > other.y)
	def update(self, entities):
		self.velocity += self.acceleration
		self.x += self.velocity.x
		self.y += self.velocity.y
		self.sprite.x = self.x
		self.sprite.y = self.y
		for ent in entities:
			if ent.affiliation == ENEMY and self.affiliation == PLAYER and (self.overlaps(ent) or ent.overlaps(self)):
				self.health -= 1	
