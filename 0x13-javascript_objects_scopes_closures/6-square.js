#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (C) {
    if (!C) {
      super.print();
    } else {
      let characters = '';
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          characters += 'C';
        }
        console.log(characters);
        characters = '';
      }
    }
  }
};
