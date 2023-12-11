#!/usr/bin/node
const [,, ...args] = process.argv;
if (args[0] === undefined) {
  console.log('0');
} else {
  const Numargs = args.map((arg) => Number(arg));
  const max = Math.max(...Numargs);
  console.log(max);
}
