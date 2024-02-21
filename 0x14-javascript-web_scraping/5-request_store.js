#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
        process.exit(1);
      }
    });
  }
});
