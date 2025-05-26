import cv2
import numpy as np

# Görseli yükle
image = cv2.imread('madenipara.jpg') 
output = image.copy()

# Gri tona çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gürültü azaltma
gray_blurred = cv2.medianBlur(gray, 7)

# Daire tespiti
circles = cv2.HoughCircles(
    gray_blurred,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=60,
    param1=100,
    param2=70,
    minRadius=60,
    maxRadius=150
)

#ÖNEMLİ NOT!!!

#param2 değerini artır → bu, dairenin merkez olma eşiği. Yükseltince daha az ama daha kesin daire bulur.

#minDist değerini biraz daha yüksek yap → birbirine yakın daireleri tek daire olarak algılasın.

#minRadius / maxRadius değerlerini gerçek para boyutuna daha uygun dar bir aralığa çek.

# Daireleri çiz ve say
count = 0
if circles is not None:
    circles = np.uint16(np.around(circles))
    count = circles.shape[1]
    for (x, y, r) in circles[0, :]:
        cv2.circle(output, (x, y), r, (0, 255, 0), 3)
        cv2.circle(output, (x, y), 3, (0, 0, 255), -1)

# Toplam sayıyı ekrana yaz
cv2.putText(output, f'Toplam Para: {count}', (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 3)

cv2.imshow('Paralar', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
