#!/usr/bin/node
const dict = require('./101-data').dict;
const myMap = new Map(Object.entries(dict));
const mySet = new Set(Object.values(dict));
const myObj = {};
for (const i of mySet) {
  const valueArr = [];
  for (const [key, value] of myMap) {
    if (i === value) {
      valueArr.push(key);
    }
    myObj[i] = valueArr;
  }
}
console.log(myObj);
