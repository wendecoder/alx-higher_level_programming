#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const l = list.length;
  let occ = 0;
  for (let i = 0; i < l; i++) {
    if (searchElement === list[i]) occ += 1;
  }
  return occ;
};
