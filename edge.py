#ソーベルオペレータとラプラシアンオペレータ
import cv2
import numpy as np
import math

Infile = 'Intest.png'#画像（画素値の配列？）で入力

print(Infile)

imgfile = cv2.imread(Infile , 1)#入力画像（カラー）の読み込み
#imgfile = cv2.imread(Infile , 0)#入力画像（グレースケール）の読み込み

cv2.namedWindow('Before')#このウィンドウのサイズを変更できるようにする
cv2.namedWindow('After1')#このウィンドウのサイズを変更できるようにする
cv2.namedWindow('After2')#このウィンドウのサイズを変更できるようにする

#メイン処理記入部分
img_tmp1 = cv2.Sobel(imgfile, cv2.CV_32F, 1 , 0)
dstfile1 = cv2.convertScaleAbs(img_tmp1)#ここまでソーベルフィルタ
img_tmp2 = cv2.Laplacian(imgfile, cv2.CV_32F, 3)
dstfile2 = cv2.convertScaleAbs(img_tmp2)

#↑出力画像の変数

cv2.imshow('Before',imgfile)#入力画像表示
cv2.imshow('After1',dstfile1)#入力画像表示
cv2.imshow('After2',dstfile2)#入力画像表示

#cv2.imwrite('Outfile.jpg', dstfile)
#出力結果の保存(ファイル名.拡張子, 実際に保存する画像の変数)
cv2.waitKey(0)#何かキーが入力されるまでここで待機
cv2.destroyAllWindows()#すべてのウィンドウを閉じる

#Opencv 画像入出力ひな形（エラーよけのためRGB-HSV変換を表示中）




