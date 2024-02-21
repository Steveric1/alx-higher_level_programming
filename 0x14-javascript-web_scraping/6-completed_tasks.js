#!/usr/bin/node
const request = require('request');
url = process.argv[2];

request(url, (error, response, body) =>{
    if (error) {
        console.log(error);
        process.exit(1);
    }
    if (response.statusCode === 200) {
        const tasks = JSON.parse(body);
        const completedTasks = tasks.filter(task => task.completed === true);
        console.log(completedTasks.length);
    }
})