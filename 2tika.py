#2値化処理
import cv2
import numpy as np
import math

Infile = 'neko.jpg'#画像（画素値の配列？）で入力

print(Infile)

#imgfile = cv2.imread(Infile , 1)#入力画像（カラー）の読み込み
imgfile = cv2.imread(Infile , 0)#入力画像（グレースケール）の読み込み

cv2.namedWindow('Before')#このウィンドウのサイズを変更できるようにする
cv2.namedWindow('After')#このウィンドウのサイズを変更できるようにする

#メイン処理記入部分
threth1 =160 #閾値
ret, dstfile = cv2.threshold(imgfile, threth1, 255, cv2.THRESH_BINARY)#(入力画像、出力画像、閾値、画素値の最大値、閾値処理の種類)
#↑出力画像の変数

cv2.imshow('Before',imgfile)#入力画像表示
cv2.imshow('After',dstfile)#入力画像表示

#cv2.imwrite('Outfile.jpg', dstfile)
#出力結果の保存(ファイル名.拡張子, 実際に保存する画像の変数)
cv2.waitKey(0)#何かキーが入力されるまでここで待機
cv2.destroyAllWindows()#すべてのウィンドウを閉じる

#Opencv 画像入出力ひな形（エラーよけのためRGB-HSV変換を表示中）


Innewfile = 'piet.png'#画像（画素値の配列？）で入力

print(Infile)

imgfile = cv2.imread(Innewfile , 1)#入力画像（カラー）の読み込み
#imgfile = cv2.imread(Infile , 0)#入力画像（グレースケール）の読み込み

#メイン処理記入部分

imgfile_hsv = cv2.cvtColor(imgfile, cv2.COLOR_BGR2HSV)#入力画像をHSV空間に変換

#閾値処理
blue_min= np.array([15,150,100], np.uint8)#符号なし8ビット整数型で配列を作成　青色閾値の最低値
blue_max= np.array([60,255,255], np.uint8)#符号なし8ビット整数型で配列を作成　青色閾値の最大値
#OpencvライブラリではHSVの色相の度合いは半分になる　青色検出の場合　通常なら180~240度だがOpencvなら90~120度となる

dstfile=cv2.inRange(imgfile_hsv, blue_min , blue_max)#指定した範囲とそれ以外の範囲を2値化する関数inRangeで２値か

#↑出力画像の変数

cv2.imshow('Before',imgfile)#入力画像表示
cv2.imshow('After',dstfile)#入力画像表示

#cv2.imwrite('Outfile.jpg', dstfile)
#出力結果の保存(ファイル名.拡張子, 実際に保存する画像の変数)
cv2.waitKey(0)#何かキーが入力されるまでここで待機
cv2.destroyAllWindows()#すべてのウィンドウを閉じる

#Opencv 画像入出力ひな形（エラーよけのためRGB-HSV変換を表示中）








