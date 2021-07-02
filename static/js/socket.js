var socket = new io(); //创建socket实例
var canvas = document.getElementById('canvas'); // 获取视频框的对象
var ctx = canvas.getContext("2d"); // 2维图像
canvas.setAttribute("width", '640px');
canvas.setAttribute("height", '480px');

var tempCanvas = document.createElement('canvas'); // 新建一个 canvas 作为缓存 canvas
var tempCtx = tempCanvas.getContext('2d');
tempCanvas.setAttribute("width", '640px');
tempCanvas.setAttribute("height", '480px');

//控制台socket接收器
socket.on('video', (data) => {
    // 获取视频帧
    let data_json = JSON.parse(data);
	let img_date_url = data_json['img_date_url']; 
    let img = new Image();
    // var img = document.getElementById('imgs');
    img.src = img_date_url;

 
    img.onload = () => {
        tempCtx.drawImage(img, 0, 0);
    }
    ctx.drawImage(tempCanvas,0,0); // 将缓存 canvas 复制到旧的 canvas

    socket.emit('video', '1');
});

socket.emit('video', '1');