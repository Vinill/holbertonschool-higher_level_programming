#!/usr/bin/node
const myArray = Number(process.argv[2]);

if (parseInt(myArray)) {
  for (let i = 0; i < myArray; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
