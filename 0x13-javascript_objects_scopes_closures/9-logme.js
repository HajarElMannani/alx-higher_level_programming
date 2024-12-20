#!/usr/bin/node
let numberArguments = 0;
exports.logMe = function (item) {
  console.log(numberArguments + ': ' + item);
  numberArguments++;
};
   

