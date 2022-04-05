#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ret = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      ret++;
    }
  }
  return ret;
};
