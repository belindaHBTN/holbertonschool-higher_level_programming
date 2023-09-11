const character = document.querySelector("#character");

async function getName() {
  const response = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
  const result = await response.json();
  // console.log(result);
  character.innerHTML = result.name;
}

getName();