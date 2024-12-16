#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;
let i;
argv.forEach((val, index) => {
  count += 1;
});
if (count === 2) {
  console.log('No argument');
} else {
  for (i = 2; i < count; i++) {
    console.log(argv[i]);
  }
}
