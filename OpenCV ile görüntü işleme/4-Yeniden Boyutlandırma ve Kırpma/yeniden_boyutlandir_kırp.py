# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 00:19:16 2024

@author: kapla
"""

import cv2

img = cv2.imread("lenna.png",1)
print("Resim boyutu:",img.shape)

cv2.imshow("Original", img)

imgResized = cv2.resize(img, (800,800))

print("Resized image shape: ",imgResized.shape)
cv2.imshow("ImageResized", imgResized)

#kırp
imgCropped = img[:200,:300]
cv2.imshow("KirpilmisResim", imgCropped)