# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:38:40 2024

@author: kapla
"""

#burada hazır öğretilmiş bir algoritma kullanılacaktır.

import cv2 
import matplotlib.pyplot as plt

#içe aktar
einstein = cv2.imread("einstein.jpg",0)
plt.figure(),plt.imshow(einstein, cmap = "gray"),plt.axis("off")

#sınıflandırıcı
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_rect = face_cascade.detectMultiScale(einstein)

for (x,y,w,h) in face_rect:
    cv2.rectangle(einstein,(x,y),(x+w,y+h), (255,255,255),10)
plt.figure(),plt.imshow(einstein, cmap="gray"),plt.axis("off")

#barcelona fotosu için yapalım şimdide
barca = cv2.imread("barcelona.jpg",0)
plt.figure(),plt.imshow(barca, cmap = "gray"),plt.axis("off")

face_rect = face_cascade.detectMultiScale(barca,minNeighbors=10)

for (x,y,w,h) in face_rect:
    cv2.rectangle(barca,(x,y),(x+w,y+h), (255,255,255),10)
plt.figure(),plt.imshow(barca, cmap="gray"),plt.axis("off")

#kolpaçino için
kolpa = cv2.imread("kolpa.jpg",0)
print(kolpa.shape)

face_rect = face_cascade.detectMultiScale(kolpa,minNeighbors=5)

for (x,y,w,h) in face_rect:
    cv2.rectangle(kolpa,(x,y),(x+w,y+h), (255,255,255),5)
plt.figure(),plt.imshow(kolpa,cmap="gray"),plt.axis("off")





#•video için capture
cap = cv2.VideoCapture(0)

while True :
    ret,frame = cap.read()
    if ret:
        face_rect = face_cascade.detectMultiScale(frame,minNeighbors=7)
        
        for (x,y,w,h) in face_rect:
            cv2.rectangle(frame,(x,y),(x+w,y+h), (255,255,255),5)
        cv2.imshow("Face dedect", frame)
        
    if cv2.waitKey(1) &  0xFF == ord("q"):break
cap.release()
cv2.destroyAllWindows()









