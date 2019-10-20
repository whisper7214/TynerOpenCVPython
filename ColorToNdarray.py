from cv2 import cv2
import numpy as np
import sys

if __name__ == "__main__":
    if len(sys.argv) > 0:
        image = cv2.imread("D:\Tyner\Python\lena.png",cv2.IMREAD_COLOR)
    else:
        print("Usqe:python RGB.py imageFile")

    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]

    cv2.imshow("b",b)
    cv2.imshow("g",g)
    cv2.imshow("r",r)

    cv2.waitKey()
    cv2.destroyAllWindows()