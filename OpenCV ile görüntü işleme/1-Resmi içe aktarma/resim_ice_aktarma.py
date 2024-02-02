# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 23:10:55 2024

@author: kapla
"""

import cv2

#içe aktarma
img = cv2.imread("messi5.jpg",0) #grasescale siyah beyaz resim

#görselleştir
cv2.imshow("ilk Resim",img)

k = cv2.waitKey(0) &0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k ==ord('s'):
    cv2.imwrite("messi_gray.png", img)
    cv2.destroyAllWindows()
