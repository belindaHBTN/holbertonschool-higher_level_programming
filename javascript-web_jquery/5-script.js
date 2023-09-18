$(function() {
  $("#add_item").click(function() {
    let item = $("<li>Item</li>");
    $(".my_list").append(item);
  })
})