let header = document.querySelector("header");
let btn = document.querySelector("#red_header");
btn.onclick = function() {
  header.setAttribute('class', 'red');
}