#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error && response && response.statusCode === 200) {
    const films = JSON.parse(body);
    let count = 0;
    films.results.forEach(function (film) {
      film.characters.forEach(function (character) {
        if (character.endsWith('/18/') || character.endsWith('/18')) count += 1;
      });
    });
    console.log(count);
  }
});
