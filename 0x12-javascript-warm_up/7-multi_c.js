#!/usr/bin/node
const { argv } = require('node:process');
const number = Number(argv[2]);
if (isNaN(parseInt(number)) === false) {
  for (let i = 0; i < argv[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
