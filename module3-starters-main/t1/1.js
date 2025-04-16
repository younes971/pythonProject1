document.addEventListener("DOMContentLoaded", () => {
    const div = document.getElementById("target");
    const html =
        `
        <li>First item</li>
        <li>Second item</li>
        <li>Third item</li>
    `;

    div.innerHTML = html;
    div.classList.add("my-list");
});
