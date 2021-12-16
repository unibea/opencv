#config :utf-8

import cv2
import numpy as np
img = cv2.imread("neko.jpg")
img2= cv2.imread("neko.jpg",0)#グレースケールで読み込む

#メイン動作1つめ：テーブルとLUT関数を使う方法
min = 100
max = 200
table = np.arange(256, dtype = np.uint8)
for i in range(256):#(0,255)だと若干あれる。(256)だとうまくいく
    table[i] = min + i * (max-min) / 255

#メイン動作２つめnormalize関数を使う方法
#min1 = 100
#max1 = 200
#img_dst2 = 0
#cv2.normalize(img, img_dst2,min,max, cv2.NORM_MINMAX) #よく分からないので確認
    
img_dst = cv2.LUT(img, table)    

cv2.imshow('before',img)
cv2.imshow('after',img_dst)        #testというウィンドウ名でimg_dstの画像を表示
#cv2.imshow('after2',img_dst2) 

cv2.waitKey(0)                    #何かキーが入力されるまでここで待機　キーが押されたら次に進む

cv2.destroyAllWindows()           #宇表示しているウィンドウをすべて消去

#コントラストを下げる　方法が2つある

