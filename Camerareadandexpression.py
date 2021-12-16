import cv2
import math
import numpy as np

#cv2.nameWindow('nyuryoku')
#cv2.nameWindow('syuturyoku')

cap = cv2.VideoCapture(1)

while True: #無限ループ
    ret, img_nyuryoku = cap.read() #カメラ映像の読み込み
    
    cv2.imshow('img_nyuryoku', img_nyuryoku)#入力画像の表示
    ch = cv2.waitKey(1) #キー？が入力されるまで待ちますという意味cv2.waitKey(キー入力の待ち時間ミリ秒)
    if ch ==ord('q'):#ord関数でord('ここの文字列をunicodeに変換する')関数
        break

cap.release()
cv2.destroyAllWindows()
    
#カメラ映像の読み込みと表示