#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, function (error, response, body) {
  if (!error && response && response.statusCode === 200) {
    const film = JSON.parse(body);
    film.characters.forEach(function (characterUrl) {
      request(characterUrl, function (error, response, body) {
        if (!error && response && response.statusCode) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
