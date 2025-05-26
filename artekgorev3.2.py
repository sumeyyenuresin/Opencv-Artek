import cv2
import numpy as np

# Görüntüyü okuma
img = cv2.imread("para2.jpg")

# Ölçeklendirme
olcek_yuzde = 40
genislik = int(img.shape[1] * olcek_yuzde / 100)
yukseklik = int(img.shape[0] * olcek_yuzde / 100)
boyut = (genislik, yukseklik)
resized = cv2.resize(img, boyut, interpolation=cv2.INTER_AREA)

# Griye çevirme ve bulanıklaştırma
gri = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
gri = cv2.medianBlur(gri, 5)

# Hough Circle Transform ile daireleri bulma
circles = cv2.HoughCircles(
    gri,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=95,
    param1=100,
    param2=35,
    minRadius=55,
    maxRadius=113
)

# Daireleri çizme ve sayma
sayi = 0
if circles is not None:
    circles = np.uint16(np.around(circles))
    for (x, y, r) in circles[0, :]:
        cv2.circle(resized, (x, y), r, (0, 255, 0), 3)
        sayi += 1

# Konsola yazdır
print(f"Para Sayısı: {sayi}")

# Görüntüyü gösterme
cv2.imshow("Sonuc", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
