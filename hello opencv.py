import numpy as np
import matplotlib.pyplot as plt
import cv2
#
car=cv2.imread('problem.jpg',cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR=1
#IMREAD_UNCHANGED=-1

cv2.imshow('problem.jpg',car)
cv2.waitKey(0)
cv2.destroyAllWindows

