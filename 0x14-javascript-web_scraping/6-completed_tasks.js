#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    let user = data[0].userId;
    let count = 0;
    const dict = {};
    for (const val of data) {
      if (user === val.userId && val.completed === true) {
        count++;
      } else if (user !== val.userId) {
	if (val.completed === true) {
	  count++;
	}
        if (count > 0) {
          dict[user] = count;
          count = 0;
        }
        if (val.completed === true) {
          count++;
        }
        user = val.userId;
      }
    }
    if (count > 0) {
      dict[user] = count;
    }
    console.log(dict);
  }
});
