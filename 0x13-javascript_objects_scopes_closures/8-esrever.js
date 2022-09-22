#!/usr/bin/node
exports.esrever = function (list) {
  const l = list.length;
  const newList = [];
  for (let i = l; i > 0; i--) {
    newList.push(list[i - 1]);
  }
  return newList;
};
