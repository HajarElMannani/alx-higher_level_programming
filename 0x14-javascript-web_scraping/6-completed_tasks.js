#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
//let fullUrl = url + '?userid';
//let dict = {}
request(url, function (error, response, body) {
    if (error) {
	console.error(error);
    }
    const bodyJson = JSON.parse(body);
let dict = {}
    bodyJson.forEach((task) => {
	if (task.completed === true) {
		dict[task.userId] += 1;
	} else {
	    dict[task.userId] = 1;
	}
    });
    console.log(dict);
});
