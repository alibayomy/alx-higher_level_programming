#!/usr/bin/node
const args = process.argv;
const num = Number(args[2]);

function factorial (num) {
  if (num < 0) {
    return -1;
  } else if (num === 1 || isNaN(num)) {
    return 1;
  } else {
    return num + factorial(num - 1);
  }
}
const val = factorial(num);
console.log(val);
