#ソーベルオペレータとラプラシアンオペレータ
import cv2
import numpy as np
import math

Infile = 'neko2.jpg'#画像（画素値の配列？）で入力

print(Infile)

cap = cv2.VideoCapture(1)

#imgfile = cv2.imread(Infile , 1)#入力画像（カラー）の読み込み
imgfile = cv2.imread(Infile , 0)#入力画像（グレースケール）の読み込み

cv2.namedWindow('Before')#このウィンドウのサイズを変更できるようにする
cv2.namedWindow('After1')#このウィンドウのサイズを変更できるようにする
cv2.namedWindow('After2')#このウィンドウのサイズを変更できるようにする
cv2.namedWindow('sirokuro')#このウィンドウのサイズを変更できるようにする
#cv2.namedWindow('noizufilter1')#このウィンドウのサイズを変更できるようにする
#cv2.namedWindow('HSV')#このウィンドウのサイズを変更できるようにする
#cv2.namedWindow('GRAY')#このウィンドウのサイズを変更できるようにする

#メイン処理記入部分
#threth1 =100 #閾値
#ret, dstfile3 = cv2.threshold(imgfile, threth1, 255, cv2.THRESH_BINARY)#(入力画像、出力画像、閾値、画素値の最大値、閾値処理の種類)

#img_tmp1 = cv2.Sobel(dstfile3, cv2.CV_32F, 1 , 0)
#dstfile1 = cv2.convertScaleAbs(img_tmp1)#ここまでソーベルフィルタ

#img_tmp2 = cv2.Laplacian(dstfile3, cv2.CV_32F, 3)
#dstfile2 = cv2.convertScaleAbs(img_tmp2)

#↑出力画像の変数
#cv2.imshow('sirokuro',dstfile3)
#cv2.imshow('Before',imgfile)#入力画像表示
#cv2.imshow('After1',dstfile1)#入力画像表示
#cv2.imshow('After2',dstfile2)#入力画像表示

while True: #無限ループ
    ret, img_nyuryoku = cap.read() #カメラ映像の読み込み
    img_hsv= cv2.cvtColor(img_nyuryoku, cv2.COLOR_BGR2HSV)#img_dstにHSVに変換
   # gray=cv2.cvtColor(img_dst,cv2.COLOR_BGR2GRAY)#入力画像をグレースケールに変換
   
   #閾値処理
    blue_min= np.array([15,150,100], np.uint8)#符号なし8ビット整数型で配列を作成　青色閾値の最低値
    blue_max= np.array([45,255,255], np.uint8)#符号なし8ビット整数型で配列を作成　青色閾値の最大値
    #OpencvライブラリではHSVの色相の度合いは半分になる　青色検出の場合　通常なら180~240度だがOpencvなら90~120度となる

    dstfile2=cv2.inRange(img_hsv, blue_min , blue_max)#指定した範囲とそれ以外の範囲を2値化する関数inRangeで２値か
    
    #contours, hierarchy = cv2.findContours(dstfile2,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #x,y,w,h = cv2.boundingRect(contours[True])
    #cv2.rectangle(img_nyuryoku,(x,y), (x+w, y+h),(0,255,0), cv2.LINE_4)
    
  
    #threth1 =150 #閾値
    #ret, dstfile3 = cv2.threshold(gray, threth1, 255, cv2.THRESH_BINARY)#ここまで2値化
    
   # element8 = np.array([[1, 1, 1],[1, 1, 1],[1, 1, 1]], np.uint8)# 8近傍
    #img_tmp = cv2.morphologyEx(dstfile3 , cv2.MORPH_OPEN, element8, iterations=1)#オープニングノイズ除去
    #dstfile = cv2.morphologyEx(img_tmp , cv2.MORPH_CLOSE, element8, iterations=1)#クロージングノイズ除去
    
    img_tmp1 = cv2.Sobel(dstfile2, cv2.CV_32F, 1 , 0)
    dstfile1 = cv2.convertScaleAbs(img_tmp1)#ここまでソーベルフィルタによる輪郭抽出
    
    img_tmp2 = cv2.Laplacian(dstfile2, cv2.CV_32F, 3)
    dstfile2 = cv2.convertScaleAbs(img_tmp2)#ここまでラプラシアンフィルタによる輪郭抽出
    
  
    cv2.imshow('sirokuro',dstfile2)#２値画像を表示
    cv2.imshow('Before',img_nyuryoku)#素のカメラ映像表示
   
    cv2.imshow('After1',dstfile1)#ソーベルフィルタ画像表示
    cv2.imshow('After2',dstfile2)#ラプラシアンフィルタ画像表示

   
    ch = cv2.waitKey(1) #キー？が入力されるまで待ちますという意味cv2.waitKey(キー入力の待ち時間ミリ秒)
    if ch ==ord('q'):#ord関数でord('ここの文字列をunicodeに変換する')関数
        break

cap.release()
cv2.destroyAllWindows()

