#!/usr/bin/node
const variable = process.argv;
if (variable[2]) {
  console.log(variable[2]);
} else {
  console.log('No argument');
}
