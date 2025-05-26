import cv2
import numpy as np

# Kamerayı başlat
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü yansıt (ayna efekti)
    frame = cv2.flip(frame, 1)

    # Renk uzayını BGR'den HSV'ye çevir
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Ten rengi için alt ve üst sınırlar (açık ten için örnek değerler)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Maske oluştur
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Gürültüyü azalt
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Konturları bul
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # En büyük konturu seç (muhtemelen el)
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(max_contour) > 1000:
            # Konturu çiz
            cv2.drawContours(frame, [max_contour], -1, (0, 255, 0), 2)

    # Görüntüleri göster
    cv2.imshow("Kamera", frame)
    cv2.imshow("Maske", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
