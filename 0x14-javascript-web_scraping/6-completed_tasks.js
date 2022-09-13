#!/usr/bin/node

const axios = require('axios');

async function Request () {
  const res = await axios.get(process.argv[2]);
  const data = res.data;
  const objs = {};

  data.forEach(element => {
    if (element.completed) objs[element.userId] = objs[element.userId] ? objs[element.userId] + 1 : 1;
  });
  console.log(objs);
}

Request();
