import pyglet

from entity import Entity, batch

window = pyglet.window.Window()
entities = [Entity(pyglet.image.load('img/image.png'), 0, 0, 32, 32)]
def update(dt):
	for ent in entities:
		ent.update(entities)
pyglet.clock.schedule_interval(update, 1 / 60.0)
@window.event
def on_draw():
	window.clear()
	batch.draw()
pyglet.app.run()

