#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is not a positive integer or equal to 0, create an empty object
      Object.create(null);
    }
  }

  print() {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate() {
    if (this.width && this.height) {
      // Exchange the width and height of the rectangle
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double() {
    if (this.width && this.height) {
      // Double the width and height of the rectangle
      this.width *= 2;
      this.height *= 2;
    }
  }
}
