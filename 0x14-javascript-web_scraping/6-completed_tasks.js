#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error && response && response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const userCompletedTasksCount = {};
    tasks.forEach(function (task) {
      if (task.completed && !userCompletedTasksCount[task.userId]) {
        userCompletedTasksCount[task.userId] = 0;
      }

      if (task.completed) userCompletedTasksCount[task.userId] += 1;
    });
    console.log(userCompletedTasksCount);
  }
});
