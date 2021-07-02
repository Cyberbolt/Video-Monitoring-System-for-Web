var socket = new io(); //创建socket实例

//控制台socket接收器
socket.on('front', (data) => {
    console.log(data);
    socket.emit('background', '1');
});

socket.emit('background', '1');