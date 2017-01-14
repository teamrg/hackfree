import pyglet

import entity
from entity import Entity, batch

window = pyglet.window.Window()
entities = [Entity(pyglet.image.load('img/image.png'), entity.PLAYER, 0, 0, 32, 32),
		Entity(pyglet.image.load('img/image.png'), entity.ENEMY, 8, 100, 32, 32)]
entities[0].velocity.y = 1
def update(dt):
	global entities
	for ent in entities:
		ent.update(entities)
	entities = list(filter(lambda x: x.health > 0, entities))
pyglet.clock.schedule_interval(update, 1 / 60.0)
@window.event
def on_draw():
	window.clear()
	batch.draw()
pyglet.app.run()

