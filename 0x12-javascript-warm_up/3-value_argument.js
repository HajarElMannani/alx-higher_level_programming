#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;

argv.forEach((val, index) => {
  count += 1;
});
if (count === 2) {
  console.log('No argument');
} else {
  for (let i = 2; i < count; i++) {
    console.log(argv[i]);
  }
}
