#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];

request(
  `https://swapi-api.alx-tools.com/api/films/${movieID}`,
  function (error, _response, body) {
    if (!error) {
      const episode = JSON.parse(body);
      console.log(episode.title);
    }
  }
);
