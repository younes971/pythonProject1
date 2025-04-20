document.getElementById('form').addEventListener('submit', async function(e) {
      e.preventDefault();
      const query = document.getElementById('searchInput').value;
      const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${query}`);
      const data = await response.json();
      const resultsDiv = document.getElementById('results');
      resultsDiv.innerHTML = '';
      data.result.forEach(joke => {
        resultsDiv.innerHTML += `<article><p>${joke.value}</p></article>`;
      });
    });