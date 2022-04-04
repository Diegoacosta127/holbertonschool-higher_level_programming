#!/usr/bin/node
const { argv } = require('process');
const arg = [];
for (let i = 2; argv[i]; i++) {
  arg.push(parseInt(argv[i]));
}
arg.sort(function (a, b) { return b - a; });
if (arg.length >= 2) {
  console.log(arg[1]);
} else {
  console.log('0');
}
