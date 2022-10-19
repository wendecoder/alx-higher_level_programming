#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (error, response, body) {
  if (!error) {
    const bodies = JSON.parse(body);
    const completed = {};
    bodies.forEach((user) => {
      if (user.completed && completed[user.userId] === undefined) {
        completed[user.userId] = 1;
      } else if (user.completed) {
        completed[user.userId] += 1;
      }
    });
    console.log(completed);
  }
});
