#!/usr/bin/node
/**
 * File: 9-add.js
 * Author: Oluwatobiloba Light
 */
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
const arg = process.argv.slice(2);
const firstArg = arg[0];
const secondArg = arg[1];
add(firstArg, secondArg);
