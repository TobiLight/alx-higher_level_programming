#!/usr/bin/node
/**
 * File: 3-rectangle.js
 * Author: Oluwatobiloba Light
 * Description:  Class Rectangle that defines a rectangle with some properties.
 */

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    // Prints the rectangle using the character X
    for (let i = 0; i < this.height; i++) {
      let x = "";
      for (let j = 0; j < this.width; j++) {
        x += "X";
      }
      console.log(x);
    }
  }
}

module.exports = Rectangle;
