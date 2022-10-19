#!/usr/bin/node
const writeme = require('fs');
writeme.writeFile(process.argv[2], process.argv[3], function (error) {
  if (error) console.log(error);
});
