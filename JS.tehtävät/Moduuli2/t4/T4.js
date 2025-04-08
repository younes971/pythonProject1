let numbers = [];

function addNumber() {
  let input = document.getElementById("num");
  let value = Number(input.value);
  if (value === 0) {
    numbers.sort((a, b) => b - a);
    let result = document.getElementById("result");
    result.innerHTML = "";
    for (let n of numbers) {
      result.innerHTML += n + "<br>";
    }
    input.disabled = true;
  } else {
    numbers.push(value);
    input.value = "";
    input.focus();
  }
}
