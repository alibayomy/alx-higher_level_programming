#!/usr/bin/node
const [,, ...args] = process.argv;
if (args[0] === undefined) {
  console.log('0');
} else {
  let Numargs = args.map((arg) => Number(arg));
  Numargs = Numargs.sort((a, b) => b - a);
  console.log(Numargs[1]);
}
