#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const obj = JSON.parse(body);
  const dict = {};

  obj.forEach((todo) => {
    if (todo.completed) {
      if (!dict(todo.userId)) {
        dict[todo.userId] = 1;
      } else {
        dict[todo.userId] += 1;
      }
    }
  });
  console.log(dict);
});
