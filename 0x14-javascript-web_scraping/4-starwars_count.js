#!/usr/bin/node
const axios = require('axios').default;
let acum = 0;
axios.get('https://swapi-api.hbtn.io/api/films/')
  .then(function (response) {
    for (let i = 0; i < response.data.results.length; i++) {
      for (let j = 0; j < response.data.results[i].characters.length; j++) {
        if (response.data.results[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
          acum += 1;
        }
      }
    }
    console.log(acum);
  })
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  });
