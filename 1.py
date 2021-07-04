from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
image = Image.open('loc_n.bmp')
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
n = np.zeros(256)
N = 0
a = np.zeros((width, height))
for i in range(width):
    for j in range(height):
        n[pix[i, j]] += 1
        N += 1
for i in range(len(n)):
    n[i] = n[i]/N
for i in range(width):
    for j in range(height):
        for k in range(pix[i, j]+1):
            a[i, j] += n[k]
        draw.point((i, j), int(a[i, j]*255))
image.save('g_equal.bmp')
s = np.zeros(256)
for i in range(256):
    for k in range(i):
        s[i] += n[k]
plt.figure(figsize=(6, 4))
plt.grid()
plt.plot(s, linewidth=0.5)
plt.show()
