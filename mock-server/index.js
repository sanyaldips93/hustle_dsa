const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const { runProductToggleScript } = require('./product_toggle');
const { runStoreToggleScript } = require('./store_toggle');
const { runMenuPushScript } = require('./redis_overload');

const app = express();
const port = 3000;

// Middleware to intercept requests
app.use((req, res, next) => {
  console.log(`Intercepted Request: ${req.method} ${req.url}`);
  // runProductToggleScript();
  // runStoreToggleScript();
  runMenuPushScript();
  res.send('Done!');
});


// Start the server
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});