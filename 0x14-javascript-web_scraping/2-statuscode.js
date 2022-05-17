#!/usr/bin/node
const argv = process.argv;
const axios = require('axios').default;
axios.get(argv[2])
  .then(function (response) {
    console.log('code: ' + response.status);
  })
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  });
