#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    let user = data[0].userId;
    const dict = {};
    for (const val of data) {
      if (val.completed) {
	  dict[val.userId] = (dict[val.userId] || 0) + 1;
      }
    }
    console.log(dict);
  }
});
