#!/usr/bin/node
/**
 * File: 3-starwars_title.js
 * Author: Oluwatobiloba Light
 * Prints the title of a Star Wars movie where the episode number matches
 * a given integer.
 */
const req = require('request');

req(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, { json: true }, (err, data, body) => {
  if (err) console.log(err);
  console.log(body.title);
});
