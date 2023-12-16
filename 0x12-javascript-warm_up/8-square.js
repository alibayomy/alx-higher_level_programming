#!/usr/bin/node
const num = process.argv[2];
if (num === undefined || isNaN(num)) {
  console.log('Missing size');
} else {
  if (num > 0) {
    let i = 0;
    while (i < num) {
      console.log('X'.repeat(num));
      i += 1;
    }
  }
}
