// app.js
const express = require('express');
const { Pool } = require('pg'); // Import the Pool class from pg

const app = express();
const PORT = process.env.PORT || 5000;

// Set up database connection
const pool = new Pool({
    user: 'postgres',        // Replace with your PostgreSQL username
    host: 'localhost',            // Replace with your PostgreSQL host
    database: 'new_database_name', // Replace with your database name
    password: 'lichess',     // Replace with your PostgreSQL password
    port: 5432                    // Default PostgreSQL port
});

// Test the database connection
pool.connect((err, client, release) => {
    if (err) {
        return console.error('Error acquiring client', err.stack);
    }
    client.query('SELECT NOW()', (err, result) => {
        release();
        if (err) {
            return console.error('Error executing query', err.stack);
        }
        console.log('Connected to PostgreSQL:', result.rows);
    });
});

// Middleware and routes (your application code goes here)
app.use(express.json());

// Example route to interact with the database
app.get('/data', async (req, res) => {
    try {
        const result = await pool.query('SELECT * FROM your_table'); // Replace with your table
        res.json(result.rows);
    } catch (error) {
        console.error('Database query error:', error);
        res.status(500).send('Server Error');
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
