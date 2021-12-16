#config :utf-8

import cv2

img = cv2.imread("Intest.png")
img2= cv2.imread("intest.png",0)#グレースケールで読み込む

#メイン動作
#　複数色チャンネルの分割
img_bgr = cv2.split(img)
#青→赤　緑→青　赤→緑に変更
img_dst = cv2.merge((img_bgr[2],img_bgr[0],img_bgr[1]))

cv2.imshow('test',img_dst)
cv2.imshow("sirokuro",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#カラー画像RGBの色の値入れ替えテスト
