import cv2
import random
from array import *
testarray = cv2.imread("image.png")

print(testarray.shape)
print(testarray)

print(type(testarray))

# So in a 1000x1000px image, that's 1 million pixels, so each pixel has 3 numbers associated with it
# (BGR), and therefore it's a 3 million number array.


