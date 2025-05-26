import cv2
import os

# Dosya adı (aynı klasörde olmalı)
cascade_path = 'haarcascade_frontalface_default.xml'

# Cascade dosyasını yükle
face_cascade = cv2.CascadeClassifier(cascade_path)

# Dosya doğru yüklendi mi kontrol et
if face_cascade.empty():
    print("Cascade dosyası yüklenemedi! Dosya mevcut mu?")
    exit()

# Kamera başlat
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kare alınamadı.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Canlı Yüz Tespiti", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
