#!/usr/bin/node
/**
 * File: 8-esrever.js
 * Author: Oluwatobiloba Light
 * Description: Returns the reversed version of a list
 */

exports.esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
