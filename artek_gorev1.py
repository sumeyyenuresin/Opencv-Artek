
import os
import subprocess
import sys


try:
    import cv2
except ImportError:
    print("OpenCV bulunamadi. Kuruluyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python"])
    import cv2

def main():
    cap = cv2.VideoCapture(0)  
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kamera görüntüsü alinamadi.")
            break

        cv2.imshow('Video', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            filename = f"frame_{frame_count}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Frame kaydedildi: {filename}")
            frame_count += 1

        if key == ord('p'):
            print("Program kapatiliyor...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
