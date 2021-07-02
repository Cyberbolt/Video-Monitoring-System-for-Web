var socket = new io(); //创建socket实例


var canvas = document.getElementById('canvas'); // 获取视频框的对象
var ctx = canvas.getContext("2d"); // 2维图像
canvas.setAttribute("width", '640px');
canvas.setAttribute("height", '480px');

//使用双缓存，防止绘图时因时间过长而闪屏
var tempCanvas = document.createElement('canvas'); // 新建一个 canvas 作为缓存 canvas
var tempCtx = tempCanvas.getContext('2d');
tempCanvas.setAttribute("width", '640px');
tempCanvas.setAttribute("height", '480px');

//控制台socket接收器
socket.on('video', (data) => {
    // 获取视频帧 将base64转为图片img
    let data_json = JSON.parse(data); //解析json数据
	let img_date_url = data_json['img_date_url']; //从后端获取图片
    let img = new Image(); //新建img实例
    img.src = img_date_url; //设置img的链接为base64格式

    //等待图片加载完成后，绘制图片到缓存区（因绘制时间较长，使用缓存区防止闪屏）
    img.onload = () => {
        tempCtx.drawImage(img, 0, 0);
    }
    ctx.drawImage(tempCanvas, 0, 0); // 将缓存 canvas 复制到旧的 canvas（复制速度远快于绘制速度，不会闪屏）

    socket.emit('video', '1'); //向后端发送请求，准备获取下一个视频帧
});


socket.emit('video', '1'); //向后端发送请求，准备获取视频帧