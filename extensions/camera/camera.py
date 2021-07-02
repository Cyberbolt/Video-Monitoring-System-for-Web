import base64

from PIL import Image
import numpy as np
import cv2 as cv


class Camera:
    def __init__(self):
        self.__cap = cv.VideoCapture(1) #连接摄像头
        self.__JPEG_HEADER = "data:image/jpeg;base64,"  # 这个是对图片转码用的

    #读取图片
    def read(self):
        ret, frame = self.__cap.read() #ret表示是否读取成功，frame是视频帧的原始np数组
        #先将数组类型编码成 jepg 类型的数据,然后转字节数组,最后将其用base64编码
        r, buf = cv.imencode(".jpeg", frame)
        dat = Image.fromarray(np.uint8(buf)).tobytes()
        img_date_url = self.__JPEG_HEADER + str(base64.b64encode(dat))[2:-1]
        return img_date_url