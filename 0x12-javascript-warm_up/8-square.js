#!/usr/bin/node
/**
 * File: 8-square.js
 * Author: Oluwatobiloba Light
 */
const arg = process.argv.slice(2);
const num = parseInt(arg[0]);

if (isNaN(num)) {
  console.log('Missing size');
}
if (!isNaN(num) && num > 0) {
  for (let i = 0; i < num; i++) {
    let output = '';
    for (let j = 0; j < num; j++) {
      output += 'X';
    }
    console.log(output);
  }
}
