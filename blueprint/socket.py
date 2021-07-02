import time

from flask import Flask, Blueprint, request, jsonify
from flask_socketio import SocketIO, emit


app = Flask(__name__)
#蓝图配置
socket = Blueprint(
    'socket', 
    __name__,
    static_folder='../static',  # 静态文件的目录
    static_url_path='',  # 静态文件目录在链接的起始位置    
)
socketio = SocketIO(async_mode='eventlet') #使用eventlet运行Websocket


@socketio.on('background')
def vedio(data):
    print(data)
    time.sleep(1)
    emit('front', '2')
