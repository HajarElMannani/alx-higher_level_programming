#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;
argv.forEach((val, index) => {
  count += 1;
});
if (count === 2) {
  console.log('undefined is undefined');
}
if (count === 3) {
  console.log(argv[2] + ' is undefined');
}
if (count === 4) {
  console.log(argv[2] + ' is ' + argv[3]);
}
