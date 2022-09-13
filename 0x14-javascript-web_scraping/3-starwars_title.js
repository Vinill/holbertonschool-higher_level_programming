#!/usr/bin/node

const axios = require('axios');

async function Request () {
  try {
    const res = await axios.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`);
    const data = res.data;
    console.log(data.title);
  } catch (error) {
    if (error) {
      console.log(error);
    }
  }
}

Request();
