#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('0');
}
const size = process.argv.length;
const myInts = [];
for (let i = 3; i < size; i++) {
  myInts[i - 3] = parseInt(process.argv[i]);
}
myInts.sort(function (a, b) { return b - a; });
console.log(myInts[1]);
