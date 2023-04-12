#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = Object.entries(dict).reduce((entries, current) => {
  if (!entries[current[1]]) {
    entries[current[1]] = [];
  }
  entries[current[1]].push(current[0]);
  return entries;
}, {});

console.log(newDict);
