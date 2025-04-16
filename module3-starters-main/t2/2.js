const target = document.getElementById('target');

const items = ['First item', 'Second item', 'Third item'];

items.forEach(text => {
    const li = document.createElement('li');
    li.textContent = text;
    target.appendChild(li);
});
