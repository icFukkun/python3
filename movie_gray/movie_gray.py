#programmed by Yuki Fukuzato

import cv2

esc = 27 #ESCのキーコード は 27 なんだメポ〜〜
fps = 30

one_window = "before"
two_window = "after"

one_file_name = "one.avi"
two_file_name = "two.avi"

one = cv2.VideoCapture(one_file_name) # 元ビデオの読み込みをするミポ〜〜

ret, one_frame = one.read()
height, width, channels = one_frame.shape
rec = cv2.VideoWriter(two_file_name, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height), False)
# .avi のコードは XVID なんだメポ〜〜(例外もあるメポ)

# ウィンドウの設定をするミポ〜〜
cv2.namedWindow(one_window)
cv2.namedWindow(two_window)

cv2.moveWindow(one_window, 20, 0)
cv2.moveWindow(two_window, 700, 0)

#変換処理のループだメポ〜〜
while ret == True:
	resized_frame = cv2.resize(one_frame, (650, 450))
	two_frame = cv2.cvtColor(resized_frame, cv2.COLOR_RGB2GRAY)

	cv2.imshow(one_window, resized_frame)
	cv2.imshow(two_window, two_frame)

	rec.write(two_frame) # フレームを書き込むミポ〜〜

	key = cv2.waitKey(66)
	if key == esc:
		break

	ret, one_frame = one.read() # 次のフレームを読み込むメポ〜〜

one.release()
rec.release() # キャプチャの解放は忘れないでミポ〜〜
cv2.destroyAllWindows()
