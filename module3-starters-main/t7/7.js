const trigger = document.getElementById("trigger");
const target = document.getElementById("target");

trigger.onmouseover = function () {
    target.src = "img/picB.jpg";
};

trigger.onmouseout = function () {
    target.src = "img/picA.jpg";
};