# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 00:12:55 2024

@author: kapla
"""

import cv2
import matplotlib.pyplot as plt

#ana görüntüyü içe aktar 
chos = cv2.imread("chocolates.jpg",0)
plt.figure(),plt.imshow(chos, cmap="gray"),plt.axis("off")

#aranacak olan görüntü 
cho = cv2.imread("nestle.jpg",0)
plt.figure(),plt.imshow(chos, cmap="gray"),plt.axis("off")

#tanımlayıcı başlatılır
#orb tanımlayıcısı (aradığımız noktanın anahtar özelliklerini arar)

orb = cv2.ORB_create()

#anahtar nokta tespiti
kp1, des1 = orb.detectAndCompute(cho,None)#none maskeleme seçilmediği için / des = description
kp2, des2 = orb.detectAndCompute(chos,None)

#brute force matcher tanımlayıcı
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
#noktaları eşleştir
matches = bf.match(des1,des2)

#mesafeye göre sırala
matches = sorted(matches, key = lambda x : x.distance)

#eşleşen resimleri görselleştirme
plt.figure()
img_match = cv2.drawMatches(cho, kp1, chos, kp2, matches[:20], None, flags=2)
plt.imshow(img_match),plt.axis("off"),plt.title("ORB")

#♣orb tanımlayıcısı ile handle etmek zordur bu yüzden sift tanımlayıcısı ile deneyelim

#sift pip install opencv-contrib-python -- user
sift = cv2.SIFT_create()
#bf 
bf = cv2.BFMatcher()

#anahtar nokta tespiti  sift ile 

kpS,desS = sift.detectAndCompute(cho,None)
kpS2,desS2 = sift.detectAndCompute(chos,None)

matches = bf.knnMatch(desS, desS2,k=2)

guzel_eslesme = []

for match1,match2 in matches :
    if match1.distance < 0.75*match2.distance:
        guzel_eslesme.append([match1])

plt.figure()
sift_matches = cv2.drawMatchesKnn(cho, kpS, chos, kpS2,guzel_eslesme, None, flags=2)
plt.imshow(sift_matches),plt.axis("off"),plt.title("SIFT")

























