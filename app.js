document.getElementById("submit").addEventListener("click", run);
frame = document.getElementById("frame");
frame.onload = function() {scrap()};
function run() {
    url = document.getElementById("url").value;
    // console.log(url);
    // frame.src=url;
}

function scrap(){
    tables = frame.contentWindow.document.querySelectorAll("table");
    console.log(tables);
}