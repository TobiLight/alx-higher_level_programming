#!/usr/bin/node
/**
 * File: 100-map.js
 * Author: Oluwatobiloba Light
 * Description: Imports an array and computes a new array.
 */

const list = require('./100-data').list;
console.log(list);
const newList = list.map((item, index) => item * index);
console.log(newList);
