#!/usr/bin/node

const axios = require('axios');
const fs = require('fs');

async function Request () {
  const fileName = process.argv[3];
  const res = await axios.get(process.argv[2], fileName);
  const data = res.data;
  fs.writeFileSync(fileName, data, (err) => console.log(err));
}

Request();
