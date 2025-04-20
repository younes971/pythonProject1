form.addEventListener("submit", async function(e) {
  e.preventDefault();
  const url = "https://api.tvmaze.com/search/shows?q=" + input.value;

  try {
      const response = await fetch(url);
      const data = await response.json();
      results.innerHTML = "";
      data.forEach(item => {
      const show = item.show;
      const image = document.createElement("img");
      if (show.image) {
          image.src = show.image.medium;
      } else {
          image.src = "https://via.placeholder.com/210x295?text=Not%20Found";
      }
      results.appendChild(img);
  });
    } catch (error) {
    console.error("Error:", error);
  } finally {
    console.log("Done");
  }
});