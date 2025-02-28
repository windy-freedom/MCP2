const express = require('express');
const path = require('path');
const app = express();
const port = 3001;

// Serve static files
app.use(express.static(path.join(__dirname)));
app.use('/images', express.static(path.join(__dirname, '..', 'images')));

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
