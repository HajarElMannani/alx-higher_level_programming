#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (C) {
      if (C === undefined) {
	  super.print();
      } else {
      let characters = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          characters += 'C';
        }
        console.log(characters);
        characters = '';
      }
    }
  }
};