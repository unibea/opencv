import cv2
import numpy as np
import math

Infile = 'neko2.jpg'#画像（画素値の配列？）で入力

print(Infile)

cap = cv2.VideoCapture(0)

#imgfile = cv2.imread(Infile , 1)#入力画像（カラー）の読み込み
imgfile = cv2.imread(Infile , 0)#入力画像（グレースケール）の読み込み

cv2.namedWindow('Before')#このウィンドウのサイズを変更できるようにする
#cv2.namedWindow('After1')#このウィンドウのサイズを変更できるようにする
#cv2.namedWindow('After2')#このウィンドウのサイズを変更できるようにする
  #cv2.namedWindow('sirokuro')#このウィンドウのサイズを変更できるようにする
#cv2.namedWindow('noizufilter1')#このウィンドウのサイズを変更できるようにする
#cv2.namedWindow('HSV')#このウィンドウのサイズを変更できるようにする
#cv2.namedWindow('GRAY')#このウィンドウのサイズを変更できるようにする


while True: #無限ループ
    ret, img_nyuryoku = cap.read() #カメラ映像の読み込み
    stl=cv2.resize(img_nyuryoku,(640,480))#画像サイズ変更
    img_hsv= cv2.cvtColor(stl, cv2.COLOR_BGR2HSV)#img_dstにHSVに変換
    #gray=cv2.cvtColor(img_dst,cv2.COLOR_BGR2GRAY)#入力画像をグレースケールに変換
   
   #閾値処理
    blue_min= np.array([15,150,100], np.uint8)#符号なし8ビット整数型で配列を作成　青色閾値の最低値
    blue_max= np.array([65,255,255], np.uint8)#符号なし8ビット整数型で配列を作成　青色閾値の最大値
    #OpencvライブラリではHSVの色相の度合いは半分になる　青色検出の場合　通常なら180~240度だがOpencvなら90~120度となる

    dstfile2=cv2.inRange(img_hsv, blue_min , blue_max)#指定した範囲とそれ以外の範囲を2値化する関数inRangeで２値か
    
    #青色部分を検出する
    contours, hierarchy = cv2.findContours(dstfile2, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for i inRange(0, len(contours)):
        if cv2.contourArea(contours[i])<500:
            continue
    if len(contours[i])>0:
        rect=contours[i]
        x,y,w,h = cv2.boundingRect(rect)
        cv2.rectangle(stl, (x,y), (x+w, y+h), (0, 255, 0))
   # print(contours)
 cv2.imshow('sirokuro',dstfile2)#２値画像を表示
cv2.imshow('Before',img_hsv)#素のカメラ映像表示
   


    ch = cv2.waitKey(1) #キー？が入力されるまで待ちますという意味cv2.waitKey(キー入力の待ち時間ミリ秒)
    if ch ==ord('q'):#ord関数でord('ここの文字列をunicodeに変換する')関数
        break

cap.release()
cv2.destroyAllWindows()


#枠囲み物体検出まで完了