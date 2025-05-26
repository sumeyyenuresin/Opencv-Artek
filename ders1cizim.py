
import cv2
import numpy as np

# 512x512 boyutunda siyah bir görüntü oluştur
canvas = np.zeros((512, 512, 3), dtype=np.uint8)

# Daire çiz (görüntü, merkez koordinatları, yarıçap, renk(BGR), kalınlık)
cv2.circle(canvas, (256, 256), 100, (0, 255, 0), -1)  # -1 = dolu daire

# Görüntüyü göster
cv2.imshow('Daire', canvas)

# Bir tuşa basana kadar bekle
cv2.waitKey(0)

# Pencereleri kapat
cv2.destroyAllWindows()
