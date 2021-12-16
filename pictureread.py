#config :utf-8
import numpy 
import cv2

img = cv2.imread("neko.jpg")
img2= cv2.imread("neko.jpg",0)#グレースケールで読み込む

cv2.imshow('test',img)
cv2.imshow("sirokuro",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#画像の読み込みと表示テスト
