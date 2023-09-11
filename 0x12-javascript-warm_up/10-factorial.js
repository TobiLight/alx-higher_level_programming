#!/usr/bin/node
/**
 * File: 10-factorial.js
 * Author: Oluwatobiloba Light
 */

function factorial (num) {
  if (isNaN(num)) return 1;
  if (num <= 1) return 1;
  return num * factorial(num - 1);
}
const arg = process.argv.slice(2);
const num = parseInt(arg[0]);
console.log(factorial(num));
