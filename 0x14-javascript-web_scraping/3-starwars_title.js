#!/usr/bin/node
const starwar = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
starwar(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
