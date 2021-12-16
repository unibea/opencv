# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:32:41 2020

@author: koroken
"""

import cv2
import numpy
img = cv2.imread("neko.jpg")
img2= cv2.imread("neko.jpg",0)#グレースケールで読み込む

#メイン動作

#ルックアップテーブルを作成
gamma =2.0 
Y = numpy.ones((256,1), dtype ='uint8') * 0 #uint8..8ビットの符号なし整数

for i in range(256):
    Y[i][0] = 255* pow(float(i) / 255, 1.0 / 2.0)
    
#ルックアップテーブル変換
img_dst = cv2.LUT(img,Y)     
print(Y)    
#ネガポジ変化
nega = 255 - img
cv2.imshow('before',img)
cv2.imshow('after',img_dst)        #testというウィンドウ名でimg_dstの画像を表示
cv2.imshow('negapoji', nega)
      
cv2.waitKey(0)                    #何かキーが入力されるまでここで待機　キーが押されたら次に進む

cv2.destroyAllWindows()           #宇表示しているウィンドウをすべて消去

#ガンマ変換テスト（ガンマ2.0）
#ネガポジ変換テスト
