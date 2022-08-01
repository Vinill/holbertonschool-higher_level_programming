#!/usr/bin/node
const variable = process.argv;
if (variable.length <= 4) {
  console.log(variable[2] + ' is ' + variable[3]);
}
