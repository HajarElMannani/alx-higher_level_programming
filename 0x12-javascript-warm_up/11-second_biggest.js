#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;
argv.forEach((val, index) => {
  count += 1;
});
if (count === 2 || count === 3) {
  console.log(0);
} else {
  argv.sort((a, b) => b - a);
  console.log(argv[3]);
}
