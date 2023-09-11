#!/usr/bin/node
/**
 * File: 101-call_me_moby.js
 * Author: Oluwatobiloba Light
 */

exports.callMeMoby = function (x, theFunction) {
  const n = parseInt(x);
  if (!isNaN(n)) {
    for (let i = 0; i < n; i++) {
      theFunction();
    }
  }
};
