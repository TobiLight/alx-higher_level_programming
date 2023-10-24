#!/usr/bin/node
/**
 * File: 0-writeme.js
 * Author: Oluwatobiloba Light
 * Writes a string to a file.
 */
const fs = require('fs');
const file = process.argv[2];
const text = process.argv[3];

try {
  fs.writeFileSync(file, text, { encoding: 'utf-8' });
} catch (error) {
  console.log(error);
}
