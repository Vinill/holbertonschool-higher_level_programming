#!/usr/bin/node

function doHeadRequest () {
    const argv = process.argv[2];
    const axios = require('axios');
  
    axios.get(argv)
      .then((response) => {
        console.log(`code: ${response.status}`);
      })
  
      .catch((error) => {
        console.log(`code: ${error.response.status}`);
      });
  }
  doHeadRequest();
  