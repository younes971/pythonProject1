doccument.addEventListener("submit", async function(e) {
  evt.preventDefault();
  const url = "https://api.tvmaze.com/search/shows?q=" + input.value;

  try {
    const response = await fetch(url);
    const data = await response.json();
  } catch (error) {
    console.log(error.message);
  } finally {
    console.log("TV show search complete.");
  }
});
