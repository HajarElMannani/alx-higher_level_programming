#!/usr/bin/node
const { argv } = require('node:process');
const number = Number(argv[2]);
const integer = parseInt(number);
if (isNaN(integer) === false) {
  console.log('My number: ' + integer);
} else {
  console.log('Not a number');
}
