#programmed by Yuki Fukuzato.

import cv2, matplotlib
import numpy as np

def read_img(name_i):
    t = 50
    img = cv2.imread(name_i)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    ret, lenna = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
    return lenna

img = read_img('lenna.jpg')

cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()
