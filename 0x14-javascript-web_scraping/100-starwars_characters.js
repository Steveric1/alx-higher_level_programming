#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async (error, response, body) => {
  if (error) {
    console.log(error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.log('Invalid:', response.statusCode);
  }

  const characters = JSON.parse(body).characters;
  const promises = characters.map(character => new Promise((resolve, reject) => {
    request(character, (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response.statusCode === 200) {
        resolve(JSON.parse(body).name);
      }
    });
  }));

  try {
    const names = await Promise.all(promises);
    names.forEach(name => console.log(name));
  } catch (error) {
    console.log(error);
  }
});
