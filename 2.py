from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
def f(z):
    #return 2/255 - z/(255**2)
    return 1/255
image = Image.open('g_7.bmp')
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
g = np.zeros(256)
n = np.zeros(256)
z = np.zeros(256)
N = 0
a = np.zeros((width, height))
for i in range(width):
    for j in range(height):
        n[pix[i, j]] += 1
        N += 1
for i in range(len(n)):
    n[i] = n[i]/N
for i in range(len(g)):
    for k in range(i):
        g[i] += f(k)
for i in range(256):
    j = 0
    while j <= 255:
        if g[j] - n[i] >= 0:
            z[i] = j
            break
        else: j += 1
for i in range(width):
    for j in range(height):
        for k in range(pix[i, j]+1):
            a[i, j] += z[k]
        draw.point((i, j), int(a[i, j]))
image.save('g_pre.bmp')
plt.figure(figsize=(6, 4))
plt.grid()
plt.plot(g*255, linewidth=0.5)
plt.show()
