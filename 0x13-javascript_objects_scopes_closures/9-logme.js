#!/usr/bin/node
/**
 * File: 9-logme.js
 * Author: Oluwatobiloba Light
 * Description: Prints the number of arguments already printed and the new
 *              argument value.
 */
let logCount = 0;
exports.logMe = function (item) {
  console.log(`${logCount}: ${item}`);
  logCount += 1;
};
