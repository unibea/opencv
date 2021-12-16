import cv2
import numpy as np
import math

Infile = 'neko.jpg'#画像（画素値の配列？）で入力

print(Infile)

imgfile = cv2.imread(Infile , 1)#入力画像（カラー）の読み込み
#imgfile = cv2.imread(Infile , 0)#入力画像（グレースケール）の読み込み

cv2.namedWindow('Before')#このウィンドウのサイズを変更できるようにする
cv2.namedWindow('After')#このウィンドウのサイズを変更できるようにする

#メイン処理記入部分
dstfile = cv2.cvtColor(imgfile, cv2.COLOR_BGR2HSV)
#↑出力画像の変数

cv2.imshow('Before',imgfile)#入力画像表示
cv2.imshow('After',dstfile)#入力画像表示

cv2.imwrite('Outfile.jpg', dstfile)
#出力結果の保存(ファイル名.拡張子, 実際に保存する画像の変数)
cv2.waitKey(0)#何かキーが入力されるまでここで待機
cv2.destroyAllWindows()#すべてのウィンドウを閉じる

#Opencv 画像入出力ひな形（エラーよけのためRGB-HSV変換を表示中）




