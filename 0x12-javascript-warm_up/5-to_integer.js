#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
if (myNum === undefined || isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log('My number: '.concat(myNum));
}
