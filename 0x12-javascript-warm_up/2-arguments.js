#!/usr/bin/node
const variable = process.argv;
if (variable.length === 3) {
  console.log('Argument found');
} else if (variable.length < 3) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
