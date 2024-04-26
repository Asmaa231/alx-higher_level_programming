#!/usr/bin/node

const x = process.argv[2];

if (x === undefined || isNaN(parseInt(x))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(x); i++) {
    console.log('C is Fun');
  }
}
