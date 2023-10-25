#!/usr/bin/node
/**
 * File: 100-starwars_characters.js
 * Author: Oluwatobiloba Light
 * Prints all characters of a Star Wars movie:
 */
const req = require('request');

req(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, { json: true }, (err, data, body) => {
  if (err) console.log(err);
  for (const character of body.characters) {
    req(character, { json: true }, (err, res, body) => {
      if (err) console.log(err);
      console.log(body.name);
    });
  }
});
