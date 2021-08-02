#!/usr/bin/node

let printTimes = parseInt(process.argv[2]);
if (printTimes !== printTimes) {
  console.log('Missing number of occurrences');
} else {
  while (printTimes > 0) {
    console.log('C is fun');
    printTimes--;
  }
}
