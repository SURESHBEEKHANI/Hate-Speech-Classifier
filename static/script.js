// JavaScript for form submission and result handling

document.getElementById('predictForm').addEventListener('submit', async function (e) {
    e.preventDefault(); // Prevents the form from submitting traditionally

    const textInput = document.getElementById('textInput').value.trim();
    const resultSection = document.getElementById('result');
    const predictionText = document.getElementById('predictionText');
    const resultTitle = document.getElementById('resultTitle');

    // Input validation
    if (!textInput) {
        alert('Please enter some text.');
        return;
    }

    try {
        // Show loading state or clear previous results
        resultSection.style.display = 'none';
        predictionText.textContent = '';
        resultTitle.textContent = '';

        // Fetch prediction result
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: textInput })
        });

        const result = await response.json();

        if (response.ok) {
            // Display prediction result
            resultTitle.textContent = 'Prediction Result:';
            predictionText.textContent = result.prediction || 'No prediction available.';
            resultSection.className = 'result-section success';
        } else {
            // Handle errors from the server
            resultTitle.textContent = 'Error:';
            predictionText.textContent = result.detail || 'An unexpected error occurred. Please try again later.';
            resultSection.className = 'result-section error';
        }

        resultSection.style.display = 'block';
    } catch (error) {
        // Handle unexpected fetch or network errors
        resultTitle.textContent = 'Error:';
        predictionText.textContent = `Failed to get prediction: ${error.message}`;
        resultSection.className = 'result-section error';
        resultSection.style.display = 'block';
    }
});

// Reset the form and result section
document.getElementById('resetBtn').addEventListener('click', () => {
    document.getElementById('predictForm').reset();
    document.getElementById('result').style.display = 'none';
});
