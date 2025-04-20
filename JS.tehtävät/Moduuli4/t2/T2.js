form.addEventListener("submit", async function(e) {
  evt.preventDefault();
  const url = "https://api.tvmaze.com/search/shows?q=" + input.value;

  try {
    const response = await fetch(url);
    const data = await response.json();
    console.log(jsonData)
  } catch (error) {
    console.log(error.message);
  }
});