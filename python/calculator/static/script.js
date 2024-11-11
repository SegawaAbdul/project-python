function calculate() {
    const display = document.getElementById('display');
    const expression = display.value;

    if (!expression) {
        alert('Please enter an expression');
        return;
    }

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ expression: expression }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            display.value = data.result;
        }
    })
    .catch(error => {
        alert('Error: ' + error);
    });
}
