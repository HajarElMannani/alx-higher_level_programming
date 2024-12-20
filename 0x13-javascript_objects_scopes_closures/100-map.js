#!/usr/bin/node
const { list } = require('./100-data.js');
const newList = list.map((x) => x * (x - 1));
console.log(list);
console.log(newList);
