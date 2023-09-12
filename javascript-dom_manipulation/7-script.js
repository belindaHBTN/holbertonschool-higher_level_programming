const movieList = document.querySelector("#list_movies");

async function getMovie() {
  const response = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
  const data = await response.json();
  // console.log(data.results);

  for (let i = 0; i < data.results.length; i++) {
    let title = document.createElement('li');
    title.innerHTML = data.results[i].title;
    movieList.appendChild(title);
  }
}

getMovie();