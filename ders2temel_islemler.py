import cv2

# Resmi yükle
image = cv2.imread('alita.jpg')  

# Resmi gri tona çevir
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny kenar algılama uygula
edges = cv2.Canny(gray_image, 50, 150)

# Görüntüleri göster
cv2.imshow('Orijinal Resim', image)
cv2.imshow('Gri Ton Resim', gray_image)
cv2.imshow('Kenar Algılama', edges)

# Bir tuşa basılana kadar bekle
cv2.waitKey(0)
cv2.destroyAllWindows()
