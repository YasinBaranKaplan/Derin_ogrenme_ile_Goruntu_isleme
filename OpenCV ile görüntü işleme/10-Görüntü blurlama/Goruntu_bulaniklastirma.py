# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:43:58 2024

@author: kapla
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np 
import warnings
warnings.filterwarnings("ignore")

#blurring ( detayı azaltır ve gürültüyü engeller)
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("original"),plt.show()

"""
ortalama bulanıklaştırma yöntemi
"""

dst2 = cv2.blur(img, ksize=(3,3))
plt.figure(),plt.imshow(dst2),plt.axis("off"),plt.title("ortalama blur")

"""
gaussian blur
"""
gb = cv2.GaussianBlur(img, ksize=(3,3),sigmaX=7)
plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("Gaussian Blur")

"""
medyan blur
"""
mb=cv2.medianBlur(img, ksize=3)
plt.figure(),plt.imshow(mb),plt.axis("off"),plt.title("Medyan Blur")

def gaussianNoise(image):
    row, col , ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image+gauss
    
    return noisy


#içe aktar ve normalize et
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255

plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("original"),plt.show()

gaussianNoisyImage = gaussianNoise(img)
plt.figure(),plt.imshow(gaussianNoisyImage),plt.axis("off"),plt.title("Gauss Noisy"),plt.show()

#gauss blur
gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize=(3,3),sigmaX=7)
plt.figure(),plt.imshow(gb2),plt.axis("off"),plt.title("with Gaussian Blur")



def saltPepperNoise(image):
    
    row, col, ch = image.shape
    s_vs_p = 0.5
    
    amount = 0.004
    
    noisy = np.copy(image)
    
    #salt beyaz piksel
    num_salt = np.ceil(amount*image.size*s_vs_p)
    coords = [np.random.randint(0,i-1,int(num_salt)) for i in image.shape]
    noisy[coords] = 1
    
    #pepper siyah
    num_pepeer = np.ceil(amount*image.size*(1 - s_vs_p))
    coords = [np.random.randint(0,i-1,int(num_pepeer)) for i in image.shape]
    noisy[coords] = 0
    
    return noisy

spImage = saltPepperNoise(img)
plt.figure(),plt.imshow(spImage),plt.axis("off"),plt.title("SP Image")





















