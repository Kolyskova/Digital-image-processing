### Исходное изображение 
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Images/1.png)  
Выведем гистограмму исходного изображения
```python
s = []
for i in range(width):
    for j in range(height):
        s.append(pix[i, j])
plt.hist(s, bins = 255)
plt.show()
```
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Graphics/h1.png)  
### Эквализация гистограммы  
```python
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
```
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Images/2.png)  
#### Гистограмма результирующего изображения  
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Graphics/h2.png)  
#### График функции преобразования яркостей  
```python
s = np.zeros(256)
for i in range(256):
    for k in range(i):
        s[i] += 255*n[k]
plt.figure(figsize=(6, 4))
plt.grid()
plt.plot(s, linewidth=0.5)
plt.show()
```
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Graphics/p1.png)  
#### График функции распределения яркостей  
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Graphics/p2.png)  
### Приведение гистограммы  
Вид заданной гистограммы (x = 255, y = 2/255)  
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Images/h.png)  
```python
def f(z):
    return 2/255 - z/(255**2)
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
```
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Images/3.png)  
#### Гистограмма результирующего изображения  
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Graphics/h3.png)  
#### График функции преобразования яркостей  
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Graphics/p3.png)  
#### График функции распределения яркостей  
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Graphics/p4.png)  

### Локальная эквализация
#### Исходное изображение и его гистограмма  
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Images/4.png)  
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Graphics/h4.png)  
```python
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
```
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Images/5.png)  
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Graphics/h5.png)  
Проведём глобальную эквализацию этого же изображения и выведем его гистограмму  
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Images/6.png)  
![](https://github.com/Kolyskova/Digital-image-processing/blob/main/Graphics/h6.png)  
