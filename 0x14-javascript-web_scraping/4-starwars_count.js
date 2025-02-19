#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const results = JSON.parse(body).results;
  if (!results) {
    console.error(error);
  }
});
const req = require('request');
const url2 = 'https://swapi-api.alx-tools.com/api/people/18/';
req(url2, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  console.log(JSON.parse(body).films.length);
});
