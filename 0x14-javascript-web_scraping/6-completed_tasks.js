#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.log('Invalid:', response.statusCode);
  }

  const completed = {};
  const tasks = JSON.parse(body);
  tasks.forEach(task => {
    if (task.completed) {
      const user = task.userId;
      completed[user] = (completed[user] || 0) + 1;
    }
  });

  console.log(completed);
});
