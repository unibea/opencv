import cv2
import numpy 

img = cv2.imread("neko.jpg")
#ヒストグラム表示用、256*100ピクセル、0で初期化
img_hst = numpy.zeros([100, 256]).astype('uint8')
rows, cols = img_hst.shape[:2]

#度数分布を求める
hdims = [256]
hranges = [0, 256]
hist = cv2.calcHist([img], [0], None, hdims, hranges)

#度数の最大値を取得
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(hist)

for i in range(0, 255):
    v = hist[i]
    cv2.line(img_hst,(i, rows), (i, rows - rows * (v / max_val)), (255, 255,255))
cv2.imshow('test',img_hst)
cv2.imshow('before',img)
cv2.waitKey(0)
cv2.destroyAllWindows()    
    #画素値のヒストグラム表示　
