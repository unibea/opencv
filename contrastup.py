#config :utf-8

import cv2
import numpy as np
img = cv2.imread("neko.jpg")
img2= cv2.imread("neko.jpg",0)#グレースケールで読み込む

min = 100
max = 250
table = np.arange(256, dtype = np.uint8)    
for i in range(0,min):
        table[i] = 0
for i in range(min,max):
        table[i] = 255 * (i - min) / (max - min)
for i in range(max,255):
        table[i] =  255

img_dst = cv2.LUT(img, table)         
        
cv2.imshow('before',img)
cv2.imshow('after',img_dst)        #testというウィンドウ名でimg_dstの画像を表示
 

cv2.waitKey(0)                    #何かキーが入力されるまでここで待機　キーが押されたら次に進む

cv2.destroyAllWindows()           #宇表示しているウィンドウをすべて消去

#コントラストを上げる



