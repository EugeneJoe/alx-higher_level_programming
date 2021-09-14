#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    for (const val of data.characters) {
      request(val, function (error, response, body1) {
        if (error) {
          console.log(error);
        } else {
          const name = JSON.parse(body1);
          console.log(name.name);
        }
      });
    }
  }
});
