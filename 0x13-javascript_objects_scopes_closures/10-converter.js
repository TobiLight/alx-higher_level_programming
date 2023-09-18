#!/usr/bin/node
/**
 * File: 10-converter.js
 * Author: Oluwatobiloba Light
 * Description: Converts a number from base 10 to another base passed as
 *              argument.
 */
exports.converter = function (base) {
  return (name) => name.toString(base);
};
