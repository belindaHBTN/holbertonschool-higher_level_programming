const btn = document.querySelector("#update_header");
const text = document.querySelector("header");

btn.onclick = function() {
  text.innerHTML = "New Header!!!";
}