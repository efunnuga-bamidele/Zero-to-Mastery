import os
from PIL import Image

imageDir = os.path.abspath(os.getcwd() +'\\scripting\\' + input("Enter directory for images to convert: ") + '\\')
convertionDir = 'scripting/' + input("Enter directory for convert: ")
# filePath = os.path.abspath(os.getcwd())
if not os.path.exists(convertionDir):
    os.makedirs(convertionDir)

try:
    for image in os.listdir(imageDir):
        if (image.endswith('.jpg')):
            convertion_file = Image.open(os.path.join(imageDir, image))
            image = image.split('.')
            convertion_file.save(f'{convertionDir}/{image[0]}.png', 'png')
            
except FileNotFoundError as err:
    print('Invalid directory specified!')
