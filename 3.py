from PIL import Image, ImageDraw
import numpy as np
image = Image.open('loc_e.bmp')
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
c = 5
n = np.zeros(256)
N = 0
a = np.zeros((width, height))
for w in range(c, width-c):
    for h in range(c, height-c):
        for i in range(w-c, w+c):
            for j in range(h-c, h+c):
                n[pix[i, j]] += 1
                N += 1
        for k in range(pix[w, h] + 1):
            a[w, h] += n[k]/N
for i in range(c, width-c):
    for j in range(c, height-c):
        draw.point((i, j), int(a[i, j]*255))
image.save('loc.bmp')
