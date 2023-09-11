#!/usr/bin/node
/**
 * File: 11-second_biggest.js
 * Author: Oluwatobiloba Light
 */
const args = process.argv.slice(2);
if (!args.length || args.length === 1) console.log(0);
else {
  let largest = -Infinity;
  let secondLargest = -Infinity;
  for (let i = 0; i < args.length; i++) {
    if (parseInt(args[i]) > largest) {
      secondLargest = largest;
      largest = parseInt(args[i]);
    } else if (
      parseInt(args[i]) > secondLargest &&
      parseInt(args[i]) < largest
    ) {
      secondLargest = parseInt(args[i]);
    }
  }
  console.log(secondLargest);
}
