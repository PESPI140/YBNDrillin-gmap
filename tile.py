from PIL import Image
import os

# Path to your image
image_path = "C:/Users/mihaj/Desktop/YBNDrillin-gmap-main/YBNDrillin-gmap/newtiles/based/lc.jpg"

# Load the image
image = Image.open(image_path)

# Define the number of tiles
num_tiles_x = 32
num_tiles_y = 32

# Get image dimensions
width, height = image.size

# Calculate tile dimensions
tile_width = width // num_tiles_x
tile_height = height // num_tiles_y

# Create a directory to save the tiles if it doesn't exist
tiles_directory = "tiles_2x2"
os.makedirs(tiles_directory, exist_ok=True)

# Save each tile
for y in range(num_tiles_y):
    for x in range(num_tiles_x):
        # Define the box for cropping
        box = (x * tile_width, y * tile_height, (x + 1) * tile_width, (y + 1) * tile_height)
        tile = image.crop(box)
        tile.save(f"{tiles_directory}/{x}_{y}.png")

print("Tiles created successfully.")
