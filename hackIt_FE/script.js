// script.js for register.html
document.getElementById('registrationForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    // Capture form data
    const formData = { 
        username: document.getElementById('username').value,
        password: document.getElementById('password').value,
        email: document.getElementById('email').value
    };

    // Convert form data to JSON
    const jsonData = JSON.stringify(formData);
    try {
        // Send POST request to backend API
        const response = await fetch('http://192.168.0.18:8000/api/v1/user/register/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: jsonData
        });

        // Handle response from backend
        const responseData = await response.json();
        console.log(responseData);
        // Handle response as needed
    } catch (error) {
        console.error('Error:', error);
        // Handle error
    }
});


// script.js for login.html
document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = {
        username: document.getElementById('loginUsername').value,
        password: document.getElementById('loginPassword').value
        
    };


    try {
        const response = await fetch('http://127.0.0.1:8000/api/v1/user/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        const data = await response.json();
        console.log(data);
        // Handle response as needed
    } catch (error) {
        console.error('Error:', error);
        // Handle error
    }
});
