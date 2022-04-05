#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const otherList = list.map((list, id) => list * id);
console.log(otherList);
