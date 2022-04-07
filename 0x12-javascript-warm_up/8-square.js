#!/usr/bin/node
const { argv } = require('process');
if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  let i, j;
  for (i = 0; i < parseInt(argv[2]); i++) {
    for (j = 0; j < parseInt(argv[2]); j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
