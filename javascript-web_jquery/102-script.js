$(function() {
  $("#btn_translate").click(function() {
    let input = $("#language_code").val();
    // console.log(input);
    $.ajax({
      type: "GET",
      url: `https://hellosalut.stefanbohacek.dev/?lang=${input}`,
      success: function(data) {
        console.log(data);
        $("#hello").text(data.hello);
      }
    })
  })
})