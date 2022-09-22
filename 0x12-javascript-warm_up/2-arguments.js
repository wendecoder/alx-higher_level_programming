#!/usr/bin/node
const myArg = process.argv.length;
if (myArg === 2) {
  console.log('No argument');
} else if (myArg === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
