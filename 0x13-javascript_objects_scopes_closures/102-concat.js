#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], function (err, data) {
  if (err) return;
  fs.writeFile(process.argv[4], data.toString(), function (_err) {});
});

fs.readFile(process.argv[3], function (err, data) {
  if (err) return;
  fs.appendFile(process.argv[4], data.toString(), function (_err) {});
});
