#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let movies = 0;
    const data = JSON.parse(body);
    for (const val of data.results) {
      if (val
        .characters
        .includes('https://swapi-api.hbtn.io/api/people/18/')) {
        movies++;
      }
    }
    console.log(movies);
  }
});
