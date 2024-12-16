#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;
argv.forEach((val, index) => {
  count += 1;
});
function add (a, b) {
  return (a + b);
}
if (count === 2 || count === 3) {
  console.log('NaN');
} else {
  console.log(add(Number(argv[2]), Number(argv[3])));
}
