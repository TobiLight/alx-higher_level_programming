#!/usr/bin/node
/**
 * File: 0-readme.js
 * Author: Oluwatobiloba Light
 * Reads and prints the content of a file.
 */
const fs = require('fs');
const file = process.argv[2];

try {
  const data = fs.readFileSync(file, 'utf-8');
  console.log(data);
} catch (error) {
  console.log(error);
}
