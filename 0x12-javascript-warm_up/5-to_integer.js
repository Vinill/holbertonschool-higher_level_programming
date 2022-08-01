#!/usr/bin/node
const variable = process.argv;
if (variable.length === 3 && parseInt(variable[2])) {
  console.log('My number: ' + parseInt(variable[2]));
} else {
  console.log('Not a number');
}
