#!/usr/bin/node
/**
 * File: 100-map.js
 * Author: Oluwatobiloba Light
 * Description: Imports an array and computes a new array.
 */

const initialList = require('./100-data').list;
const newList = initialList.map((item, idx) => {
  return idx * item;
});
console.log(initialList);
console.log(newList);
