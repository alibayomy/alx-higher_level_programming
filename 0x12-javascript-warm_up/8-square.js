#!/usr/bin/node
const num = process.argv[2];
if (num === undefined) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < num) {
    console.log('X'.repeat(num));
    i += 1;
  }
}
