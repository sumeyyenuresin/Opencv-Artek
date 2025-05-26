import cv2
import numpy as np

# Tuval oluştur (siyah zemin)
canvas = np.zeros((500, 500, 3), dtype="uint8")

# Kalp şekli denklemi (parametrik)
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Koordinatları resim boyutuna göre ölçekle
x = x * 10 + 250
y = -y * 10 + 250  # y eksenini ters çeviriyoruz (görüntü sistemi için)

# Noktaları birleştirerek çokgen çiz
pts = np.array(list(zip(x.astype(int), y.astype(int))), np.int32)
pts = pts.reshape((-1, 1, 2))

# Kalbi çiz 
cv2.fillPoly(canvas, [pts], (0, 0, 255))

cv2.imshow("Kalp", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
