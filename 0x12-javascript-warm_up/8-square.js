#!/usr/bin/node
const myArg = parseInt(process.argv[2]);
let str = '';
if (myArg === undefined || isNaN(myArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myArg; i++) {
    str = '';
    for (let j = 0; j < myArg; j++) str += 'X';
    console.log(str);
  }
}
