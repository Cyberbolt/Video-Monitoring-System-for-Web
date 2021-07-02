from flask import Flask, Blueprint, request, jsonify


app = Flask(__name__)
#蓝图配置
home = Blueprint(
    'home', 
    __name__,
    static_folder='../static',  # 静态文件的目录
    static_url_path='',  # 静态文件目录在链接的起始位置    
)


@home.route('/')
def homes():
    return home.send_static_file('index.html')