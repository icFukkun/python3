#programmed by Yuki Fukuzato
#フレーム間差分法

import cv2
import numpy as np

esc = 27 #ESCのキーコード は 27
fps = 30
frame = None # フレーム取得用変数

one_window = "before"
two_window = "after"

one_file_name = "one.avi"
two_file_name = "two.avi"

one = cv2.VideoCapture(0) # 元ビデオの読み込み

ret, one_frame = one.read()
height, width, channels = one_frame.shape
rec = cv2.VideoWriter(two_file_name, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height), False)
# .avi のコードは XVID

# ウィンドウの設定
cv2.namedWindow(one_window)
cv2.namedWindow(two_window)

cv2.moveWindow(one_window, 20, 0)
cv2.moveWindow(two_window, 700, 0)

#変換処理のループ
while ret == True:
	resized_frame = cv2.resize(one_frame, (650, 450))
	gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_RGB2GRAY)

	if frame is None:
		frame = gray_frame.copy().astype("float")
		continue # frameに値が入っていなければ, frameに現在のフレームを取得する

	cv2.accumulateWeighted(gray_frame, frame, 0.01) # 現在のフレームと移動平均との差を計算
	delta_frame = cv2.absdiff(gray_frame, cv2.convertScaleAbs(frame)) # absdiff = 2つの画像の絶対値差分 

	flag, thresh_frame = cv2.threshold(delta_frame, 40, 255, cv2.THRESH_BINARY)
	mask_frame = cv2.medianBlur(thresh_frame.copy(), 3)
	img, contours, hierarchy = cv2.findContours(mask_frame.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	# findContours = 2値化画像の輪郭
	# RETE_EXTERNAL = 最も外側の輪郭のみ抽出
	# CHAIN_APPROX_SIMPLE = 輪郭を圧縮し, 冗長点の情報を削除してメモリ消費を抑える.
	# CHAIN_APPROX_NONE = 輪郭上の全点の情報を保持

	two_frame = cv2.drawContours(resized_frame.copy(), contours, -1, (0, 255, 0), 3)

	cv2.imshow(one_window, resized_frame)
	cv2.imshow(two_window, two_frame)

	rec.write(two_frame) # フレームを書き込む

	key = cv2.waitKey(1) # 60 msec の間入力がなければ次のフレームへ
	if key == esc:
		break

	ret, one_frame = one.read() # 次のフレームを読み込む

one.release()
rec.release() # キャプチャの解放
cv2.destroyAllWindows()
