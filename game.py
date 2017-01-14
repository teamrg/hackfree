import pyglet

import entity
from entity import *

window = pyglet.window.Window()

fall_speed = 2
bkg_tile_height = 32

alien_tex = pyglet.image.load('img/alien.png')
cloud_tex = pyglet.image.load('img/cloud.png')
player_tex = pyglet.image.load('img/rover.png')

entities = [Entity(player_tex, entity.PLAYER, 320, 400, 32, 32),
		Entity(pyglet.image.load('img/image.png'), entity.ENEMY, 8, 100, 32, 32),
		Entity(alien_tex, entity.ALIEN, 100, 100, 64, 32)]
lives = []
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
def spawn_cloud(x):
	entities.append(Entity(cloud_tex, entity.ENEMY, x, 0, 64, 16))

spawn_cloud(400)

def update(dt):
	global lives
	if len(lives) != entities[0].health:
		lives = []
		for i in range(entities[0].health):
			life = pyglet.sprite.Sprite(player_tex, batch = batch, x = i * 48, y = 16, group = foreground)
			life.scale = 0.5
			lives.append(life)
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

