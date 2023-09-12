#!/usr/bin/node
/**
 * File: 5-square.js
 * Author: Oluwatobiloba Light
 * Description: Class Square that defines a square and inherits from Rectangle
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
