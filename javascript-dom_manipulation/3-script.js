let header = document.querySelector("header");
let flag = true;
let btn = document.querySelector("#toggle_header");
btn.onclick = function() {
  flag = !flag;
  if (flag) {
    header.setAttribute('class', 'green');
  } else {
    header.setAttribute('class', 'red');
  }

}