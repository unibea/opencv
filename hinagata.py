import cv2
import math
import numpy as np

cv2. namedWindow('Before')
cv2. namedWindow('After')

cap = cv2.VideoCapture(0) #カメラ0番でcapに読み込み開始


while True:
    ret, imgfile = cap.read()  #カメラ映像の読み込み 
    img_dst = cv2.cvtColor(imgfile, cv2.COLOR_BGR2HSV)
    #img_dstにHSVに変換したカメラ画像を挿入(メイン処理)
    
    cv2.imshow('Before', imgfile)
    cv2.imshow('After', img_dst)

    ch = cv2.waitKey(1)
    if ch == ord('q'):
        break
    
cap.release() #カメラ読み込み停止
cv2.destroyAllWindows()    
