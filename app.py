#防止网络库出问题
import eventlet
eventlet.monkey_patch()

from datetime import timedelta

from flask import Flask

from blueprint import socketio #导入socket实例
#导入蓝本
from blueprint import home
from blueprint import socket


def create_app():
    app = Flask( __name__)
    app.secret_key = 'dk~fu@hfv%7x4Fc1' #session密钥
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7) #session有效期14天
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1) #禁用缓存 #仅开发使用
    app.register_blueprint(home) #导入home蓝本
    app.register_blueprint(socket) #导入socet蓝本
    socketio.init_app(app)
    
    return socketio, app


if __name__ == '__main__':
    socketio, app = create_app()
    # app.run(host='127.0.0.1', port='5000')
    socketio.run(app=app, host='127.0.0.1', port='5000')