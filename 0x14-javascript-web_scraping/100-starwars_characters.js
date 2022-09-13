#!/usr/bin/node

const axios = require('axios');

async function getName (element) {
  const res = await axios.get(element);
  const name = res.data.name;
  console.log(name);
}

async function Request () {
  const res = await axios.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`);
  const data = res.data;
  data.characters.forEach(element => {
    getName(element);
  });
}

Request();