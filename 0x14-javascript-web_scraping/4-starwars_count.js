#!/usr/bin/node
/**
 * File: 4-starwars_count.js
 * Author: Oluwatobiloba Light
 * Prints the number of movies where the character “Wedge Antilles” is present.
 */
const req = require('request');

req(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  const moviesCount = body.split('/people/18/').length - 1;
  console.log(moviesCount);
});
