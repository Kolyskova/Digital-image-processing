from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
image = Image.open('loc_e.bmp')
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
s = []
for i in range(width):
    for j in range(height):
        s.append(pix[i, j])
plt.hist(s, bins = 255)
plt.show()
