// server.js
const express = require('express');
const axios = require('axios');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Serve register.html for /register route
app.get('/register', (req, res) => {
    res.sendFile(__dirname + '/register.html');
});

// Serve login.html for /login route
app.get('/login', (req, res) => {
    res.sendFile(__dirname + '/login.html');
});

// Handle user registration
app.post('/register', async (req, res) => {
    try {
        const response = await axios.post('http://192.168.0.18:8000/api/v1/user/register/', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(400).json({ error: error.response.data });
    }
});

// Handle user login
app.post('/login', async (req, res) => {
    try {
        const response = await axios.post('http://192.168.0.18:8000/api/v1/user/login/', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(400).json({ error: error.response.data });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
