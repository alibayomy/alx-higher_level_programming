#!/usr/bin/node
const args = process.argv;
function pr (args) {
  if (args.length === 2) {
    console.log('No argument');
  } else if (args.length === 3) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}
pr(args);
