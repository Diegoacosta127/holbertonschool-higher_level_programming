#!/usr/bin/node
exports.converter = function (base) {
  return function newFunction (number) {
    return number.toString(base);
  };
};
