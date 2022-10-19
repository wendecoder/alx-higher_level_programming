#!/usr/bin/node
const req = require('request');
req('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    orderprint(characters, 0);
  }
});

function orderprint (characters, index) {
  req(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        orderprint(characters, index + 1);
      }
    }
  });
}
