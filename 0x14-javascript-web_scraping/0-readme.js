#!/usr/bin/node
const readme = require('fs');
readme.readFile(process.argv[2], 'utf8', function (content, error) {
  console.log(content || error);
});
