#!/usr/bin/node
/**
 * File: 6-square.js
 * Author: Oluwatobiloba Light
 * Description: Class Square that defines a square and inherits from Square
 */
const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    // Prints the rectangle using the character c
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        if (!c) {
          x += 'X';
        } else {
          x += c;
        }
      }
      console.log(x);
    }
  }
}
module.exports = Square;
