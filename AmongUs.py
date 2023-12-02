import pyglet
from pyglet.window import key

# Window setup
window = pyglet.window.Window(1000, 600, "Among Tasks")

# Load map
map_image = pyglet.image.load("map.png")
map_sprite = pyglet.sprite.Sprite(map_image)

# Load character sprite and resize
character_image = pyglet.image.load("character-1.png")
character_scale = 0.1  # Adjust this value to resize your character
character = pyglet.sprite.Sprite(character_image, x=500, y=400)
character.scale = character_scale

# Character speed
speed = 5

# Key state handling
key_handler = key.KeyStateHandler()
window.push_handlers(key_handler)


def update(dt):
    if key_handler[key.LEFT] or key_handler[key.A]:
        character.x -= speed
    if key_handler[key.RIGHT] or key_handler[key.D]:
        character.x += speed
    if key_handler[key.UP] or key_handler[key.W]:
        character.y += speed
    if key_handler[key.DOWN] or key_handler[key.S]:
        character.y -= speed

    # Boundary conditions
    if character.x < 0:
        character.x = 0
    if character.y < 0:
        character.y = 0
    if character.x > window.width - character.width:
        character.x = window.width - character.width
    if character.y > window.height - character.height:
        character.y = window.height - character.height


# Update the game 60 times per second
pyglet.clock.schedule_interval(update, 1 / 60.0)


@window.event
def on_draw():
    window.clear()
    map_sprite.draw()  # Draw the map
    character.draw()  # Draw the character


# Run the game
pyglet.app.run()
