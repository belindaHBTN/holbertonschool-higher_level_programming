$(function() {
  $("#add_item").click(function() {
    $(".my_list").append("<li>Item</li>");
  })

  $("#remove_item").click(function() {
    $(".my_list li:last").remove();
  })

  $("#clear_list").click(function() {
    let items = $(".my_list").children();
    if (items.length > 0) {
      $.each(items, function(index, item) {
        item.remove();
      })
    }
  })
})