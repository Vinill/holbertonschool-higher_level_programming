#!/usr/bin/node
const myArray = Number(process.argv[2]);
const str = 'X';
if (parseInt(myArray)) {
  for (let i = 0; i < myArray; i++) {
    console.log(str.repeat(myArray));
  }
} else {
  console.log('Missing size');
}
