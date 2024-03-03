import cv2
import numpy as np

# kamera aç
cap = cv2.VideoCapture(0)

# bir tane frame oku
ret, frame = cap.read()

if not ret:
    print("Kamera başlatılamadı.")
    exit()

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")    

while True:
    # frame oku
    ret, frame = cap.read()
    
    if not ret:
        print("Frame alınamadı.")
        break
    
    # tespit işlemi
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # nesne tespiti yapıldıysa
    if len(faces) > 0:
        for (x,y,w,h) in faces:
            track_window = (x, y, w, h)  # başlangıç penceresi
            break  # ilk yüzü seç
            
        # region of interest
        roi = frame[y:y+h, x:x+w]
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
        cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

        term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Frame alınamadı.")
                break
            
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

            ret, track_window = cv2.meanShift(dst, track_window, term_crit)

            x, y, w, h = track_window
            img2 = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
            
            cv2.imshow("Takip", img2)
            
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    else:
        cv2.imshow("Kamera", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Temizleme
cap.release()
cv2.destroyAllWindows()
