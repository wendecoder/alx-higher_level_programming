#!/usr/bin/node
const req = require('request');
req.get(process.argv[2]).on('response', response => {
  console.log(`code: ${response.statusCode}`);
});
