$(function() {
  let $movies = $("#list_movies");

  $.ajax({
    type: "GET",
    url: "https://swapi-api.hbtn.io/api/films/?format=json",
    success: function(data) {
      console.log(data.results);
      $.each(data.results, function(index, film) {
        $movies.append(`<li>${film.title}</li>`);
      })
    }
  })
})