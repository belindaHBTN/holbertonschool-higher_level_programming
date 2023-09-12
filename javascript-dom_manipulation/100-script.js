window.addEventListener("load", () => {
  const myList = document.querySelector(".my_list");
  const addBtn = document.querySelector("#add_item");
  const removeBtn = document.querySelector("#remove_item");
  const clearBtn = document.querySelector("#clear_list");

  addBtn.onclick = () => {
    const item = document.createElement("li");
    item.textContent = "Item";
    myList.appendChild(item);
  }

  removeBtn.onclick = () => {
    myList.removeChild(myList.children[myList.children.length - 1]);
  }

  clearBtn.onclick = () => {
    while (myList.firstChild) {
      myList.removeChild(myList.firstChild);
    }
  }
})