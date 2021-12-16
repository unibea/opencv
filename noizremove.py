#膨張収縮を繰り返したオープニング・クロージングノイズ除去
import cv2
import numpy as np
import math

Infile = 'neko2.jpg'#画像（画素値の配列？）で入力

#imgfile = cv2.imread(Infile , 1)#入力画像（カラー）の読み込み
imgfile = cv2.imread(Infile , 0)#入力画像（グレースケール）の読み込み

cv2.namedWindow('Before')#このウィンドウのサイズを変更できるようにする
cv2.namedWindow('After')#このウィンドウのサイズを変更できるようにする

#メイン処理記入部分
#2値化処理
threth1 =140 #閾値
ret, dstfile1 = cv2.threshold(imgfile, threth1, 255, cv2.THRESH_BINARY)#(入力画像、出力画像、閾値、画素値の最大値、閾値処理の種類)
#膨張、収縮処理
#element4 = np.array([[0, 1, 0],[1, 1, 1],[0, 1, 0]], np.uint8)# 4近傍
element8 = np.array([[1, 1, 1],[1, 1, 1],[1, 1, 1]], np.uint8)# 8近傍

img_tmp = cv2.morphologyEx(dstfile1 , cv2.MORPH_OPEN, element8, iterations=1)
dstfile = cv2.morphologyEx(img_tmp , cv2.MORPH_CLOSE, element8, iterations=1)

cv2.imshow('Before',dstfile1)#入力画像表示
cv2.imshow('After',dstfile)#入力画像表示

#cv2.imwrite('Outfile.jpg', dstfile)
#出力結果の保存(ファイル名.拡張子, 実際に保存する画像の変数)
cv2.waitKey(0)#何かキーが入力されるまでここで待機
cv2.destroyAllWindows()#すべてのウィンドウを閉じる

#Opencv 画像入出力ひな形（エラーよけのためRGB-HSV変換を表示中）




