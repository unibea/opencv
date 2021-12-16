#空間フィルタ処理 平均化フィルタによる画像平滑化
import cv2
img = cv2.imread("Intest.png") #imgにテスト用の画像（画素値の配列）を挿入

print(img)

img_dst = cv2.blur(img, (3, 3))

cv2.imshow("Before", img)
cv2.imshow("After",img_dst )

cv2.waitKey(0)
cv2.destroyAllWindows()


