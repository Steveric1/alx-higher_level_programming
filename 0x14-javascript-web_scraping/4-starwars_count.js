#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  if (response.statusCode !== 200) {
    console.log('Invalid:', response.statusCode);
  }

  let count = 0;

  const films = JSON.parse(body).results;
  films.forEach(film => {
    const characters = film.characters;
    if (characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  });
  console.log(count);
});
