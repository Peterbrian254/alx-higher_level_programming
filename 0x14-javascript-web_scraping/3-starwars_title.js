#!/usr/bin/node
const request = require('request');
request(`http://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if ((error)) { return console.log(body.title); }
  body = JSON.parse(body);
  console.log(body.title);
});
