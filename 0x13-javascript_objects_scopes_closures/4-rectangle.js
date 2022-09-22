#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let i = 0; i < this.height; i++) {
      str = '';
      for (let j = 0; j < this.width; j++) str += 'X';
      console.log(str);
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const w = this.width;
    const h = this.height;
    this.width = h;
    this.height = w;
  }
};
