#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numberOccurences = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      numberOccurences++;
    }
  }
  return (numberOccurences);
};
