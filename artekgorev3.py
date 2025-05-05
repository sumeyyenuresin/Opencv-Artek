import cv2
import numpy as np

image = cv2.imread('para.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için bulanıklaştırma 
blurred = cv2.GaussianBlur(gray, (15, 15), 0)

# Hough Circle Transform ile daireleri algıla (hassasiyet artırıldı)
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1.2, 30, param1=80, param2=40, minRadius=15, maxRadius=45)

# Eğer daireler tespit edildiyse ekrana yazdır
if circles is not None:
    circles = np.uint16(np.around(circles))
    print(f'Bulunan madeni para sayısı: {len(circles[0])}')
    for (x, y, r) in circles[0]:
        cv2.circle(image, (x, y), r, (0, 255, 0), 3)

cv2.imshow('Detected Coins', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
