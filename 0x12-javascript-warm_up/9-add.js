#!/usr/bin/node
const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);

function add (x, y) {
  console.log(x + y);
}
add(x, y);
