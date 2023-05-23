#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieID}`;

function logCharacters (characters, index) {
  if (index >= characters.length) return;

  request(characters[index], function (error, response, body) {
    if (!error && response && response.statusCode) {
      const character = JSON.parse(body);
      console.log(character.name);
      logCharacters(characters, index + 1);
    }
  });
}

request(url, function (error, response, body) {
  if (!error && response && response.statusCode) {
    const film = JSON.parse(body);
    logCharacters(film.characters, 0);
  }
});
