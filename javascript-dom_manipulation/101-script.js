window.addEventListener("load", () => {
  const btn = document.querySelector("#btn_translate");
  const output = document.querySelector("#hello");
  const selectedOption = document.querySelector("#language_code");

  btn.onclick = () => {
    let value = selectedOption.value;

    fetch(`https://hellosalut.stefanbohacek.dev/?lang=${value}`)
      .then(response => {
        return response.json()
      })
      .then(data => {
        output.textContent = data.hello;
      })
  }
})