#!/usr/bin/node
/**
 * File: 2-rectangle.js
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
}

module.exports = Rectangle;
