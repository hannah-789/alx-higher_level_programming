#!/usr/bin/node

const Rectangle = require('./4-rectangle'); // Assuming the Rectangle class is in the file '4-rectangle.js'

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }
}

module.exports = Square;

