#!/usr/bin/node
const mySize = process.argv.length;
if (mySize <= 3) {
  console.log(0);
} else {
  const myArray = process.argv.map(Number);
  myArray.slice(2, mySize);
  myArray.sort((a, b) => a - b);
  console.log(myArray[myArray.length - 2]);
}
