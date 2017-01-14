import pyglet

import entity
from entity import Entity, batch, background

window = pyglet.window.Window()

entities = [Entity(pyglet.image.load('img/rover.png'), entity.PLAYER, 0, 480, 32, 32),
		Entity(pyglet.image.load('img/image.png'), entity.ENEMY, 8, 100, 32, 32),
		Entity(pyglet.image.load('img/alien.png'), entity.ALIEN, 100, 100, 64, 32)]
entities[0].velocity.y = -1
entities[0].health = 3
bkg = []

def add_background(image):
	global bkg
	bkg = []
	for i in range(0, 640, image.width):
		for j in range(0, 480, image.height):
			bkg.append(pyglet.sprite.Sprite(image, batch= batch, x = i, y = j, group = background))
add_background(pyglet.image.load('img/space.png'))

def update(dt):
	global entities
	for ent in entities:
		ent.update(entities)
	entities = list(filter(lambda x: x.health > 0, entities))

pyglet.clock.schedule_interval(update, 1 / 60.0)
@window.event
def on_key_press(symbol, modifiers):
	if symbol == pyglet.window.key.D:
		entities[0].velocity.x = 4
	if symbol == pyglet.window.key.A:
		entities[0].velocity.x = -4
@window.event
def on_key_release(symbol, modifiers):
	if symbol == pyglet.window.key.D or symbol == pyglet.window.key.A:
		entities[0].velocity.x = 0
@window.event
def on_draw():
	window.clear()
	batch.draw()
pyglet.app.run()

