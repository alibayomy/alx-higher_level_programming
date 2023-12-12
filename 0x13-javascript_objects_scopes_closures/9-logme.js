#!/usr/bin/node
let printedSoFar = 0;
exports.logMe = function (item) {
  console.log(`${printedSoFar}: ${item}`);
  printedSoFar++;
};
