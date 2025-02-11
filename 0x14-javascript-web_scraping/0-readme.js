#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
console.log(file);

fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
