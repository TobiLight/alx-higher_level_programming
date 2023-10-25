#!/usr/bin/node
/**
 * File: 5-request_store.js
 * Author: Oluwatobiloba Light
 * Gets the contents of a webpage and stores it in a file.
 */
const req = require('request');
const fs = require('fs');

req(process.argv[2], (err, data, body) => {
  if (err) console.log(err);
  try {
    fs.writeFileSync(process.argv[3], body, { encoding: 'utf8' });
  } catch (err) {
    console.error(err);
  }
});
