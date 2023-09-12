#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/**
 * File: 5-square.js
 * Author: Oluwatobiloba Light
 * Description: Class Square that defines a square and inherits from Rectangle
 */

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}

module.exports = Square;
