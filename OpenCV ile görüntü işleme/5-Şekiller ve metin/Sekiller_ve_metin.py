# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 00:46:35 2024

@author: kapla
"""

import cv2
import numpy as np

#resim oluştur
img = np.zeros((512,512,3),np.uint8)#♣siyah bir resim oluşacak
print(img.shape)

cv2.imshow("siyah", img)

#cizgi
#(resim,başlangıç noktası,bitiş noktası, renk,kalınlık)
cv2.line(img,(0,0),(512,512),(0,255,0),3)#BGR =(255,0,0)Kırmızı  (0,0,255)Mavi  (0,255,0)
cv2.imshow("Cizgili", img)

#dikdörtgen
#(başlangıç,bitiş , renk,(opsiyonel olarak içini doldurma))
cv2.rectangle(img, (0,0), (256,256),(255,0,0),cv2.FILLED)
cv2.imshow("Dikdortgen",img)

#daire
#(resim,merkez,yarıçap,renk,(opsiyonel olarak içi dolu))
cv2.circle(img, (300,300), 45, (0,0,255),cv2.FILLED)
cv2.imshow("Cember", img)

#metin 
#(resim,başlangıç noktası, font, kalınlığı,renk
cv2.putText(img, "text", (350,350), cv2.FONT_HERSHEY_COMPLEX,1, (255,255,255))
cv2.imshow("Metinli", img)