#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const tasks = JSON.parse(body);
  const dict = {};
  tasks.forEach((task) => {
    if (task.completed) {
      if (dict[task.userId] === undefined) {
        dict[task.userId] = 1;
      } else {
        dict[task.userId] += 1;
      }
    }
  });
  console.log(dict);
});
