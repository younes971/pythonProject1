document.getElementById("source").addEventListener("submit", function (event) {
    event.preventDefault();

    const firstName = document.querySelector('input[name="firstname"]').value;
    const lastName = document.querySelector('input[name="lastname"]').value;

    document.getElementById("target").textContent = `Your name is ${firstName} ${lastName}`;
});
