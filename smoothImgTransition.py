#! /usr/bin/env python

import numpy as np
import cv2
import time

img1 = cv2.imread('man2.jpg')
img2 = cv2.imread('raf2.jpg')

val = 1
inc = 0.01


while True:
    dst = cv2.addWeighted(img1, val, img2, 1-val, 0)
    cv2.imshow('dst',dst)
    cv2.waitKey(1)
    
    if val < 0 or val > 1:
        inc = -inc
        time.sleep(0.7)
    
    val += inc
    print val
    time.sleep(0.01)

cv2.destroyAllWindows()
        
