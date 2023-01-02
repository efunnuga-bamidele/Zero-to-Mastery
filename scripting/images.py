from PIL import Image, ImageFilter


# img = Image.open('E:\Study Projects\Python\Zero-to-Mastery\scripting\pokedex\pikachu.jpg')
img = Image.open('E:\Study Projects\Python\Zero-to-Mastery\scripting\\astro.jpg')


# filtered_image = img.filter(ImageFilter.SHARPEN)
# filtered_image = img.convert('L')
# rotate = filtered_image.rotate(90);
# resize = filtered_image.resize((300, 300))
print(img)
# box = (100, 100, 400, 400)
# cropped = filtered_image.crop(box)

# cropped.save("cropped.png", 'png')
# cropped.show()

img.thumbnail((400, 400))
img.save('tumbnail.png', 'png')