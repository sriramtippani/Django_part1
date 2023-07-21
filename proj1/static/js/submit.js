var a1 = document.querySelector('h1');
var a2 = document.querySelector('h3');

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var symbol = '#';

    for(var i = 0; i < 6; i = i + 1) {
        r = Math.floor(Math.random() * 16);
        symbol = symbol + letters[r];
    }
    return symbol
}

function changeColor() {
    a1.style.color = getRandomColor();
    a2.style.color = getRandomColor();
}
setInterval(changeColor, 1000)