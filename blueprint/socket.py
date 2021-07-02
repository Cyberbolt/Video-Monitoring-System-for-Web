import time
import json

from flask import Flask, Blueprint, request, jsonify
from flask_socketio import SocketIO, emit

from extensions import Camera


app = Flask(__name__)
#蓝图配置
socket = Blueprint(
    'socket', 
    __name__,
    static_folder='../static',  # 静态文件的目录
    static_url_path='',  # 静态文件目录在链接的起始位置    
)
socketio = SocketIO(async_mode='eventlet') #使用eventlet运行Websocket
camera = Camera() #实例化相机类


@socketio.on('video')
def vedio(data):
    time.sleep(0.001)
    img_date_url = camera.read() #获取视频帧
    data = json.dumps({
        'img_date_url': img_date_url
    })
    emit('video', data, json=True)
