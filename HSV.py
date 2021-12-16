#config :utf-8

import cv2

#img = cv2.imread("Intest.png")
#img2= cv2.imread("intest.png",0)#グレースケールで読み込む
cap = cv2.VideoCapture(1) #capにカメラ画像読み込み


#メイン動作
#img_dst= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#img_dstにHSVに変換したimgを挿入

while True: #無限ループ
    ret, img_nyuryoku = cap.read() #カメラ映像の読み込み
    img_dst= cv2.cvtColor(img_nyuryoku, cv2.COLOR_BGR2HSV)#img_dstにHSVに変換したカメラ画像を挿入
    
    cv2.imshow('img_nyuryoku', img_dst)#入力画像の表示
    
    ch = cv2.waitKey(1)
    
    if ch ==ord('q'):
        break
  

#cv2.imshow('before',img)
#cv2.imshow('after',img_dst)        #testというウィンドウ名でimg_dstの画像を表示
#cv2.imshow("sirokuro",img2)       #sirokuroというウィンドウ名でimgという画像を表示

#cv2.waitKey(0)                    #何かキーが入力されるまでここで待機　キーが押されたら次に進む

cv2.destroyAllWindows()           #宇表示しているウィンドウをすべて消去

#カラー画像のRGBをHSVに変換テスト
#カメラ映像をリアルタイムでHSVに変換テスト