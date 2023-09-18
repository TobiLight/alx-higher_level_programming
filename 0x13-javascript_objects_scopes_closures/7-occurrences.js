#!/usr/bin/node
/**
 * File: 7-occurrences.js
 * Author: Oluwatobiloba Light
 * Description: Returns the number of occurrences in a list
 */

exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurence += 1;
    }
  }
  return occurence;
};
