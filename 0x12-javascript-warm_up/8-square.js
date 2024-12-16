#!/usr/bin/node
const { argv } = require('node:process');
const number = Number(argv[2]);
let text = '';
if (isNaN(parseInt(number)) === false) {
  for (let i = 0; i < argv[2]; i++) {
    for (let j = 0; j < argv[2]; j++) {
      text += 'X';
    }
    console.log(text);
    text = '';
  }
} else {
  console.log('Missing size');
}
