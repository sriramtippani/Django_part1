var a1 = document.querySelector('h1');
var a2 = document.querySelector('h2');
var a4 = document.querySelector('p');
var a5 = document.querySelector('ol');

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
    a4.style.color = getRandomColor();
    a5.style.color = getRandomColor();
}
setInterval(changeColor, 1000)


var dateUTC = new Date();
var dateUTC = dateUTC.getTime() 
var dateIST = new Date(dateUTC);
//date shifting for IST timezone (+5 hours and 30 minutes)
dateIST.setHours(dateIST.getHours()); 
dateIST.setMinutes(dateIST.getMinutes());
document.getElementById("demo").innerHTML = 'Date: ' + dateIST.toDateString();



var currentTime = new Date()
var hours = currentTime.getHours()
var minutes = currentTime.getMinutes()
var seconds = currentTime.getSeconds()
if (minutes < 10){
    minutes = "0" + minutes
}
var t_str = hours + ":" + minutes + ":" + seconds;
if(hours > 11){
    t_str += "PM";
} else {
   t_str += "AM";
}
document.getElementById("semo").innerHTML = 'time: ' + t_str;