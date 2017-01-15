import pyglet
import random
import sys

import entity
from entity import *
import music

window = pyglet.window.Window(height = 700)

fall_speed = 1
bkg_tile_height = 32

player_tex = pyglet.image.load('img/rover.png')
player_l_tex = pyglet.image.load('img/rover-left.png')
player_boost_tex = pyglet.image.load('img/rover-boost.png')
player_boost_l_tex = pyglet.image.load('img/rover-boost-left.png')
player_bullet_tex = pyglet.image.load('img/player-bullet.png')
alien_tex = pyglet.image.load('img/alien.png')
cloud_tex = pyglet.image.load('img/cloud.png')
bullet_tex = pyglet.image.load('img/bullet.png')
powerup_tex = pyglet.image.load('img/powerup.png')

entities = [Entity(player_tex, entity.PLAYER, window.width / 2, window.height - 80, 64, 64),
		Entity(alien_tex, entity.ALIEN, 100, 0, 64, 8)]
lives = []
entities[0].health = 3
bkg = []

def add_background(image):
	global bkg
	bkg = []
	bkg_tile_height = image.height
	for i in range(0, window.width, image.width):
		for j in range(-image.height, window.height + image.height, image.height):
			bkg.append(pyglet.sprite.Sprite(image, batch= batch, x = i, y = j, group = background))
add_background(pyglet.image.load('img/space.png'))

def spawn_alien(x):
	entities.append(Entity(alien_tex, entity.ALIEN, x, 0, 64, 8))
def spawn_bullet(x):
	ent = Entity(bullet_tex, entity.ENEMY, x, 0, 8, 8)
	ent.velocity.y = 8
	entities.append(ent)
def spawn_player_bullet():
	ent = Entity(player_bullet_tex, entity.FRIENDLY, entities[0].x, entities[0].y, 8, 8)
	ent.velocity.y = -4
	entities.append(ent)
def spawn_cloud(x):
	entities.append(Entity(cloud_tex, entity.ENEMY, x, 0, 64, 48))
def spawn_powerup(x):
	ent = Entity(powerup_tex, entity.POWERUP, x, 0, 16, 16)
def spawn_enemy():
	value = random.randint(0, 2)
	x = random.randint(0, window.width)
	spawns = [ spawn_alien, spawn_bullet, spawn_cloud]
	spawns[value](x)

spawn_cloud(400)
spawn_bullet(100)

def update(dt):
	global lives, entities, joystick
	if len(lives) != entities[0].health:
		lives = []
		for i in range(entities[0].health):
			life = pyglet.sprite.Sprite(player_tex, batch = batch, x = i * 32, y = 16, group = foreground)
			life.scale = 0.5
			lives.append(life)
	for sprite in bkg:
		sprite.y += fall_speed
		if sprite.y % bkg_tile_height == 0:
			sprite.y -= bkg_tile_height
	for ent in entities:
		ent.update(entities)
	if len(entities) < 3:
		spawn_alien(320)
	value = joystick.x
	if value > 0.2:
		set_player_sprite(player_boost_tex)
		entities[0].flip = False
	elif value < -0.2:
		set_player_sprite(player_boost_l_tex)
		entities[0].flip = True
	else:
		if entities[0].flip:
			set_player_sprite(player_l_tex)
		else:
			set_player_sprite(player_tex)
	entities[0].velocity.x = 4 * value
	entities = list(filter(lambda x: x.health > 0 and x.y < window.height, entities))

pyglet.clock.schedule_interval(update, 1 / 60.0)
def set_player_sprite(img):
	entities[0].sprite = pyglet.sprite.Sprite(img, x = entities[0].x, y = entities[0].y, batch = batch, group = foreground)
joysticks = pyglet.input.get_joysticks()
if len(joysticks) > 0:
	joystick = joysticks[0]
	joystick.open()
	@joystick.event
	def on_joybutton_press(joystick, button):
		spawn_player_bullet()

@window.event
def on_key_press(symbol, modifiers):
	if symbol == pyglet.window.key.D:
		entities[0].velocity.x = 4
		set_player_sprite(player_boost_tex)
	if symbol == pyglet.window.key.A:
		entities[0].velocity.x = -4
		set_player_sprite(player_boost_l_tex)
@window.event
def on_key_release(symbol, modifiers):
	if symbol == pyglet.window.key.D:
		entities[0].velocity.x = 0
		set_player_sprite(player_tex)
	if symbol == pyglet.window.key.A:
		entities[0].velocity.x = 0
		set_player_sprite(player_l_tex)
	if symbol == pyglet.window.key.SPACE:
		spawn_player_bullet()
def music_step_happened():
	step = music.clusters.pop(0)
	if step == 0:
		pass
	elif step == 1:
		spawn_enemy()
	elif step == 2:
		spawn_powerup(random.randint(0, window.width))
pyglet.clock.schedule_interval(music_step_happened, 40 * 0.001)

@window.event
def on_draw():
	window.clear()
	batch.draw()
song = pyglet.media.load(sys.argv[1])
song.play()
pyglet.app.run()

