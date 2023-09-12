#!/usr/bin/node
/**
 * File: 101-sorted.js
 * Author: Oluwatobiloba Light
 * Description: Imports a dictionary of occurrences by user id and computes
 *              a dictionary of user ids by occurrence
 */
const dict = require("./101-data").dict;
const entries = Object.entries(dict);
const newDict = {};

for (const userId in dict) {
  const occurrenceCount = dict[userId];
  if (newDict.hasOwnProperty(occurrenceCount)) {
    newDict[occurrenceCount].push(userId);
  } else {
    newDict[occurrenceCount] = [userId];
  }
}
console.log(newDict);
