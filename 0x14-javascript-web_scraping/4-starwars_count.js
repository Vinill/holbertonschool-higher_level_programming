#!/usr/bin/node

const axios = require('axios');

async function Request () {
  const res = await axios.get(process.argv[2]);
  const data = res.data;
  console.log(
    data.results.filter((film) =>
      film.characters.some((char) => /18/.test(char))
    ).length
  );
}

Request();
