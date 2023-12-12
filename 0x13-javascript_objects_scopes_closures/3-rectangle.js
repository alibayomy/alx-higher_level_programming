#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let y = 0;
    while (y < this.height) {
      console.log('X'.repeat(this.width));
      y++;
    }
  }
}
module.exports = Rectangle;
