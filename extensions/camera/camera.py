import numpy as np
import cv2 as cv


class Camera:
    def __init__(self):
        self.__cap = cv.VideoCapture(1) #连接摄像头

    def read(self):
        ret, frame = self.__cap.read()
        print()