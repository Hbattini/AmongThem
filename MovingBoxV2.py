import pyglet
from pyglet.window import key

# Constants
WIDTH, HEIGHT = 400, 400
BLOCK_SIZE = 50
WHITE = (255, 255, 255,1)
FPS = 60

# Create the window
window = pyglet.window.Window(width=WIDTH, height=HEIGHT, caption="Move the Block")
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Initialize game variables
block_x = (WIDTH - BLOCK_SIZE) // 2
block_y = (HEIGHT - BLOCK_SIZE) // 2
block_speed = 5

# Create a sprite for the block
block_image = pyglet.image.SolidColorImagePattern(color=WHITE)
block_texture = block_image.create_image(BLOCK_SIZE, BLOCK_SIZE).get_texture()
block_sprite = pyglet.sprite.Sprite(block_texture, x=block_x, y=block_y)

# Set up the game loop
def update(dt):
    global block_x, block_y

    # Move the block
    if keys[key.LEFT] and block_x > 0:
        block_x -= block_speed
    if keys[key.RIGHT] and block_x < WIDTH - BLOCK_SIZE:
        block_x += block_speed
    if keys[key.UP] and block_y < HEIGHT - BLOCK_SIZE:
        block_y += block_speed
    if keys[key.DOWN] and block_y > 0:
        block_y -= block_speed

    # Update the sprite position
    block_sprite.x = block_x
    block_sprite.y = block_y

# Set up the drawing function
def draw():
    window.clear()
    block_sprite.draw()

# Schedule the update and draw functions
pyglet.clock.schedule_interval(update, 1/FPS)
# pyglet.clock.set_fps_limit(FPS)

# Run the application
pyglet.app.run()
