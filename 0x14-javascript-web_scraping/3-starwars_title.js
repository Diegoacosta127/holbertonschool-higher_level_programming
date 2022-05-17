#!/usr/bin/node
const argv = process.argv;
const axios = require('axios').default;
axios.get('https://swapi-api.hbtn.io/api/films/' + argv[2] + '/')
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  });
