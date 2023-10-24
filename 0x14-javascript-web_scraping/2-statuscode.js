#!/usr/bin/node
/**
 * File: 2-statuscode.js
 * Author: Oluwatobiloba Light
 * Displays the status code of a GET request.
 */
const req = require('request');

req(process.argv[2], (err, data) => {
  if (err) console.log(err);
  console.log("code:", data.statusCode);
});
