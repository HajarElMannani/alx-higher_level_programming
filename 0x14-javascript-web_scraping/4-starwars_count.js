#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, function (error, response, body) {
  if (error) {
      console.error(error);
      return;
  }
  console.log(JSON.parse(body).films.length);
});
