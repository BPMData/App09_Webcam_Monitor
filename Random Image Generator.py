import numpy as np
import cv2
#
# def pixel(default=None):
#     output = random.randint(0, 255)
#     return output
#
# test3 = arr.array('i', [[[pixel() for _ in range(3)] for _ in range(4)] for _ in range(4)])
#
# print(test3)
# test = arr.array('i', [10,20,30])
#
# print(test)
#
# test2 = arr.array('i', [pixel() for _ in range(3)])



def pixel():
    output = np.random.randint(0, 255)
    return output

# test3 = np.array([[[pixel() for _ in range(3)] for _ in range(100)] for _ in range(100)])
test4 = np.array([[[pixel() for _ in range(3)] for _ in range(1920)] for _ in range(1080)])
print(test4)
print(test4.shape)

cv2.imwrite("randdesktop.png", test4)


# (1920*1080)/(100*75) = 7,500
#
# 100*75 = 750
#
# 1920*1080 = 2,073,600