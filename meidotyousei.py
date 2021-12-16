#config :utf-8

import cv2
import numpy as np
img = cv2.imread("neko.jpg")
img2= cv2.imread("neko.jpg",0)#グレースケールで読み込む

#メイン動作
shift = 100
table = np.arange(256, dtype = np.uint8)#numpyにより等差数列？を作成
for i in range(0,255):
    j = i + shift
    if j < 0:
        table[i] = 0
    elif j > 255:
        table[i] = 255
    else:
        table[i] = j#ｊが0未満なら０、255より上なら２５５にしてテーブルに値を代入する
        
img_dst = cv2.LUT(img, table)        #LUT関数によって計算する？

cv2.imshow('before',img)
cv2.imshow('after',img_dst)        #testというウィンドウ名でimg_dstの画像を表示
#cv2.imshow("sirokuro",img2)       #sirokuroというウィンドウ名でimgという画像を表示

cv2.waitKey(0)                    #何かキーが入力されるまでここで待機　キーが押されたら次に進む

cv2.destroyAllWindows()           #宇表示しているウィンドウをすべて消去

#明度を上げるテスト

