import cv2
import numpy as np

image_path = "para3.jpg"
original = cv2.imread(image_path)

gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (11, 11), 0)

dp = 1.1
minDist = 45
param1 = 90
param2 = 48
minRadius = 35
maxRadius = 75

output = original.copy()

circles = cv2.HoughCircles(
    blur,
    cv2.HOUGH_GRADIENT,
    dp,
    minDist,
    param1=param1,
    param2=param2,
    minRadius=minRadius,
    maxRadius=maxRadius
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 2)  # sadece yeşil kontür
    count = len(circles[0])
    print(f"Algılanan para sayısı: {count}")
else:
    print("Hiç para algılanamadı.")

cv2.imshow("Coin Detector", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
