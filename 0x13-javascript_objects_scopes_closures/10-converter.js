#!/usr/bin/node
exports.converter = function (base) {
  function helper (num) {
    return num.toString(base);
  }
  return (helper);
};
