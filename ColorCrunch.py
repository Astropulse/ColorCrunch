import argparse
from PIL import Image

parser = argparse.ArgumentParser(
    description="Convert an image to pure black and white"
)
parser.add_argument("input_file", help="Path to the input image (PNG, JPEG, etc.)")
parser.add_argument("output_file", help="Path to save the processed image")

args = parser.parse_args()

# Open the input image
input_image = Image.open(args.input_file)

# Quantize images to 2 colors
input_image = input_image.quantize(colors=2, method=1, kmeans=2, dither=0).convert('RGB')

# Find the brightest color and darkest color, convert them to white and black
pixels = list(input_image.getdata())
darkest, brightest = min(pixels), max(pixels)

# Map darkest pixel to 0 (black), brightest to 255 (white), and leave others as is
new_pixels = [0 if pixel == darkest else 255 if pixel == brightest else pixel for pixel in pixels]

# Create a new image in "L" (grayscale) mode and put our transformed pixels in
new_image = Image.new("L", input_image.size)
new_image.putdata(new_pixels)

# Convert the new image to RGB and save
input_image = new_image.convert('RGB')
input_image.save(args.output_file)

print(f"Processed image saved to {args.output_file}")