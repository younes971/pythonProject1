let numbers = [];

function addNumber() {
  let input = document.getElementById("num");
  let value = Number(input.value);

  if (numbers.includes(value)) {
    document.getElementById("result").innerHTML =
      "Number already exist. Given numbers:<br>" +
      numbers.sort((a, b) => a - b).join("<br>");
    input.disabled = true;
  } else {
    numbers.push(value);
    input.value = "";
  }
}
