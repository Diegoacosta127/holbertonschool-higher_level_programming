#!/usr/bin/node
const argv = process.argv;
const axios = require('axios').default;
let done = 0;
const dict = Object();
axios.get(argv[2])
  .then(function (response) {
    for (let i = 0; response.data[i]; i++) {
      if (i !== 0) {
        if (response.data[i].userId !== response.data[i - 1].userId) {
          done = 0;
        }
      }
      if (response.data[i].completed === true) {
        done += 1;
      }
      dict[response.data[i].userId] = done;
    }
    console.log(dict);
  });
