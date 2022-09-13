#!/usr/bin/node

function doHeadRequest () {
    const movie = process.argv[2];
    const url = `https://swapi-api.hbtn.io/api/films/${movie}`;
    const axios = require('axios');
  
    try {
        const res = axios.get(url);
        const data = res.data;
        console.log(data.title);
    } catch (error) {
        console.log(error);
    }
  }
  doHeadRequest();
  