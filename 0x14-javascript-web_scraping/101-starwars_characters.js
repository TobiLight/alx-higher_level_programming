#!/usr/bin/node
/**
 * File: 101-starwars_characters.js
 * Author: Oluwatobiloba Light
 * Prints all characters of a Star Wars movie:
 */
const req = require('request');
const util = require('util');

const asyncreq = util.promisify(req);

(async () => {
  try {
    const body = (await asyncreq(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, { json: true })).body;
    for (const url of body.characters) {
      const body = (await asyncreq(url, { json: true })).body;
      console.log(body.name);
    }
  } catch (err) {
    console.log(err);
  }
})();
