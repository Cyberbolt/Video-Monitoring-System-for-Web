# Video-Monitoring-System-for-Web
基于web的视频监控系统，可以调用本地或外置摄像头进行实时视频监控。

使用方法:

进入项目根目录，创建 Python 虚拟环境，输入

python -m venv venv

激活虚拟环境

. venv/bin/activate (Windows 输入 venv\Scripts\activate)

安装依赖

pip install -r requirements.txt

之后输入

python app.py

运行此程序，浏览器访问 127.0.0.1:5000 即可

如果您连接的外置摄像头，请在 config/config.py 中修改摄像头的序号
