var t = null;
t = setTimeout(time, 1000);
function time() {
    var weeks = new Array("Sun", "Mon", "Tues", "Wed", "Thur", "Fri", "Sat")
    clearTimeout(t);
    dt = new Date();
    var year = dt.getFullYear();
    var month = dt.getMonth() + 1;
    var day = dt.getDate();
    var weekday = weeks[dt.getDay()];
    var hr = dt.getHours();
    var min = dt.getMinutes();
    var sec = dt.getSeconds();
    document.querySelector(".showTime").innerHTML = 
    "Time: " + day + "-" + month + "-" + year + " " + weekday + " " +
    hr + " hr:" + min + "min:" + sec + "sec";
    t = setTimeout(time, 1000);
}