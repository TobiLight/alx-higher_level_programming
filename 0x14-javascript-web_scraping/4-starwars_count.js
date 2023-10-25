#!/usr/bin/node
/**
 * File: 4-starwars_count.js
 * Author: Oluwatobiloba Light
 * Prints the number of movies where the character “Wedge Antilles” is present.
 */
const req = require('request');

req(url, (err, res, body) => {
  if (err) console.log(err);
  const movies_count = body.split('/people/18/').length - 1;
  console.log(movies_count);
});
