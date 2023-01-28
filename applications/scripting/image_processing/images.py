from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
print(f"Format: {img.format}")
print(f"Size: {img.size}")
print(f"MODE: {img.mode}")
# print(dir(img))

# Filtering
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")

# Change mode
converted_img = img.convert('L')
converted_img.save("converted.png", "png")

# Rotate
rotated_img = converted_img.rotate(90)
rotated_img.save("rotated.png", "png")

# Resize
resized_img = converted_img.resize((300, 300))
resized_img.save("resized.png", "png")

# Crop
cropped_img = converted_img.crop((0, 0 ,300, 300))
cropped_img.save("cropped.png", "png")
