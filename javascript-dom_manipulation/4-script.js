const list = document.querySelector(".my_list");
const btn = document.querySelector("#add_item");

btn.onclick = function() {
  const item = document.createElement("li");
  item.innerHTML = "Item";
  list.appendChild(item);
}