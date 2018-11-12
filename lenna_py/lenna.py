#programmed by Yuki Fukuzato.

import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

def read_img(name_i):
    img = cv2.imread(name_i)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img

img = read_img('lenna.jpg')

cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()
