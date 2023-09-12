#!/usr/bin/node
/**
 * File: 100-map.js
 * Author: Oluwatobiloba Light
 * Description: Imports an array and computes a new array.
 */

const initialList = require('./100-data').list;
console.log(initialList);
console.log(initialList.map((item, idx) => item * idx));
