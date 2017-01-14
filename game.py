import pyglet

import entity
from entity import Entity, batch, background

window = pyglet.window.Window()

fall_speed = 2
bkg_tile_height = 32

alien_tex = pyglet.image.load('img/alien.png')

entities = [Entity(pyglet.image.load('img/rover.png'), entity.PLAYER, 320, 400, 32, 32),
		Entity(pyglet.image.load('img/image.png'), entity.ENEMY, 8, 100, 32, 32),
		Entity(alien_tex, entity.ALIEN, 100, 100, 64, 32)]
entities[0].health = 3
bkg = []

def add_background(image):
	global bkg
	bkg = []
	bkg_tile_height = image.height
	for i in range(0, 640, image.width):
		for j in range(-image.height, 480, image.height):
			bkg.append(pyglet.sprite.Sprite(image, batch= batch, x = i, y = j, group = background))
add_background(pyglet.image.load('img/space.png'))

def spawn_alien(x):
	entities.append(Entity(alien_tex, entity.ALIEN, x, 0, 64, 32))

def update(dt):
	for sprite in bkg:
		sprite.y += fall_speed
		if sprite.y % bkg_tile_height == 0:
			sprite.y -= bkg_tile_height
	global entities
	for ent in entities:
		ent.update(entities)
	if len(entities) < 3:
		spawn_alien(320)
	entities = list(filter(lambda x: x.health > 0 and x.y < window.height, entities))

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

