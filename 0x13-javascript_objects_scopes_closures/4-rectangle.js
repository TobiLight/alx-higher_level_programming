#!/usr/bin/node
/**
 * File: 4-rectangle.js
 * Author: Oluwatobiloba Light
 * Description:  Class Rectangle that defines a rectangle with some properties.
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // Prints the rectangle using the character X
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x += 'X';
      }
      console.log(x);
    }
  }

  rotate () {
    // Exchanges the width and the height of the rectangle
    const width = this.width;
    const height = this.height;
    this.width = height;
    this.height = width;
  }

  double () {
    // Multiples the width and the height of the rectangle by 2
    const dobuleWidth = this.width * 2;
    const doubleHeight = this.height * 2;
    this.width = dobuleWidth;
    this.height = doubleHeight;
  }
}

module.exports = Rectangle;
