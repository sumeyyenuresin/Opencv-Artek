import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)  
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  
        
        lower_color = np.array([100, 100, 100])  # Alt sınır (H, S, V)
        upper_color = np.array([140, 255, 255])  # Üst sınır (H, S, V)
        
        mask = cv2.inRange(hsv, lower_color, upper_color)  # Renk maskeleme
        result = cv2.bitwise_and(frame, frame, mask=mask)  # Orijinal görüntüyle maskeyi uygula
        
        # Kontur bulma
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Küçük konturları filtrele
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Dikdörtgen çiz
        
        cv2.imshow('Frame', frame)
        cv2.imshow('Mask', mask)
        cv2.imshow('Result', result)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()