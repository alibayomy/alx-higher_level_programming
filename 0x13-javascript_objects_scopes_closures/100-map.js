#!/usr/bin/node
const List = require('./100-data').list;
console.log(List);
const newList = List.map((a, index) => a * index);
console.log(newList);
