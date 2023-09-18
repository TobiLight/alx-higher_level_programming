#!/usr/bin/node
/**
 * File: 102-add_me_maybe.js
 * Author: Oluwatobiloba Light
 */
exports.addMeMaybe = function (x, theFunction) {
  const n = parseInt(x);
  if (!isNaN(n)) {
    theFunction(n + 1);
  }
};
