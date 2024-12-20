#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (C) {
    if (C) {
      let characters = '';
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.width; j++) {
          characters += 'C';
        }
        console.log(characters);
        characters = '';
      }
    } else {
      super.print();
    }
  }
};
