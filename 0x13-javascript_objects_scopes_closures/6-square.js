#!/usr/bin/node
const SquareP = require('./5-square');
class Square extends SquareP {
  charPrint (c = 'X') {
    let i = 0;
    while (i < this.width) {
      console.log(c.repeat(this.width));
      i++;
    }
  }
}
module.exports = Square;
