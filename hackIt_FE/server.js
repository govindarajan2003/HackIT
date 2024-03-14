// server.js
const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
const PORT = process.env.PORT || 3000;
const DJANGO_API_URL = "http://your-django-api-url/login"; // Update this with your Django API endpoint URL

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Serve HTML file
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

// Handle login POST request
app.post("/login", async (req, res) => {
  try {
    const { username, password } = req.body;
    // Forward login details to Django API
    const response = await axios.post(DJANGO_API_URL, { username, password });
    res.json(response.data); // Send back the response from Django API
  } catch (error) {
    console.error("Error:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
