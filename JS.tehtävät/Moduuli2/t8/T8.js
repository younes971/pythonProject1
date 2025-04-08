function concat(array) {
  let result = "";
  for (let i = 0; i < array.length; i++) {
    result += array[i];
  }
  return result;
}
const names = ["Johnny", "DeeDee", "Joey", "Marky"];
document.getElementById("result").textContent = combined;