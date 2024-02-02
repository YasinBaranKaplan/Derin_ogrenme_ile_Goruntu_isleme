# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:25:30 2024

@author: kapla
"""

import cv2
import matplotlib.pyplot as plt

#karıştırma
img1 = cv2.imread("img1.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("img2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1,(600,600))
print(img1.shape)
img2 = cv2.resize(img2,(600,600))
print(img2.shape)


#karıştırlmış resim = alpha*img1 + beta*img2
blended = cv2.addWeighted(img1,0.5,img2,0.5,0)#değerleri değiştirerek baskınlık arttırılıp azaltılabilir
plt.figure()
plt.imshow(blended)
