let dogNames = [];

for (let i = 0; i < 6; i++) {
  dogNames.push(prompt(`Enter the name of dog ${i + 1}:`));
}

dogNames.sort().reverse();

const ul = document.getElementById('dogList');
dogNames.forEach(name => {
});
