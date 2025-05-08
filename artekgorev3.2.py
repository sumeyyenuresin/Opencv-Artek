import cv2
import numpy as np

image = cv2.imread('para2.jpg')
cv2.imshow('Orijinal Görüntü', image)
cv2.imwrite('1_orijinal.jpg', image)

# Griye çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gri Görüntü', gray)
cv2.imwrite('2_gri.jpg', gray)

# Gaussian blur uygula
blurred = cv2.GaussianBlur(gray, (15, 15), 0)
cv2.imshow('Bulanıklaştırılmış', blurred)
cv2.imwrite('3_bulanik.jpg', blurred)

# Daire tespiti (Hough)
circles = cv2.HoughCircles(
    blurred,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=60,
    param1=100,
    param2=40,
    minRadius=30,
    maxRadius=100
)

output = image.copy()
filtered_circles = []

# Daireleri filtrele ve çiz
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    # Yakın merkezli daireleri filtrele
    for c in circles:
        x, y, r = c
        too_close = False
        for fc in filtered_circles:
            fx, fy, fr = fc
            if np.sqrt((x - fx)**2 + (y - fy)**2) < 30:  # merkezler çok yakınsa atla
                too_close = True
                break
        if not too_close:
            filtered_circles.append((x, y, r))

    for (x, y, r) in filtered_circles:
        cv2.circle(output, (x, y), r, (0, 255, 0), 2)    # dış daire
        cv2.circle(output, (x, y), 2, (0, 0, 255), 3)    # merkez

    print(f'Tespit edilen para sayısı: {len(filtered_circles)}')
else:
    print("Hiç para bulunamadı.")

cv2.imshow('Tespit Edilen Paralar', output)
cv2.imwrite('4_sonuc.jpg', output)

cv2.waitKey(0)
cv2.destroyAllWindows()
