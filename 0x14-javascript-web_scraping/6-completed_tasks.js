#!/usr/bin/node
/**
 * File: 6-completed_tasks.js
 * Author: Oluwatobiloba Light
 * Computes the number of tasks completed by user id.
 */
const req = require('request');

req(process.argv[2], { json: true }, (err, data, body) => {
  if (err) console.log(err);
  const results = {};
  for (const task of body) {
    if (task.completed) {
      results[task.userId] = (results[task.userId] || 0) + 1;
    }
  }
  console.log(results);
});
