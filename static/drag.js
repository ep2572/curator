var dv = document.getElementById('textbox');
var x = 0;
var y = 0;
var l = 0;
var t = 0;
var isDown = false;

dv.onmousedown = function(e) {
    x = e.clientX;
    y = e.clientY;

    l = dv.offsetLeft;
    t = dv.offsetTop;
    isDown = true;
    dv.style.cursor = 'move';
}

window.onmousemove = function(e) {
    if (isDown == false) {
        return;
    }

    var nx = e.clientX;
    var ny = e.clientY;

    var nl = nx - (x - l);
    var nt = ny - (y - t);

    dv.style.left = nl + 'px';
    dv.style.top = nt + 'px';
}

dv.onmouseup = function() {
    isDown = false;
    dv.style.cursor = 'default';
}