# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 12:51:54 2024

@author: kapla
"""

import cv2 
import numpy as np

img = cv2.imread("lenna.png")
cv2.imshow("original", img)

hor = np.hstack((img,img))#yanyana ekleme
cv2.imshow("Horizontal", hor)

ver = np.vstack((img,img))
cv2.imshow("Vertical", ver)