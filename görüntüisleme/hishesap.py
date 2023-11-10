import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntü yükle
foto = cv2.imread('.\image\dogaresmi.jpeg',0)
print(foto.shape)

height, width = foto.shape

histogram = np.zeros(256)
print(histogram)

# Histogramda tüm pikseller için yoğunluk arttırma
for x in range(height):
    for y in range(width):
        histogram[foto[x, y]] += 1

