#!/usr/bin/node
/**
 * File: 102-concat.js
 * Author: Oluwatobiloba Light
 * Description: Concats 2 files.
 */

const fs = require('fs');
const args = process.argv.slice(2);

function concatFiles (arg) {
  const fileA = args[0];
  const fileB = args[1];
  const fileC = args[2];
  if (!args.length) return;
  fs.readFile(`${fileA}`, 'utf-8', (err, data1) => {
    if (err) throw err;
    fs.readFile(`${fileB}`, 'utf-8', (err, data2) => {
      const concatData = data1 + '\n' + data2 + '\n';
      fs.writeFile(`${fileC}`, concatData, 'utf-8', (err) => {
        if (err) throw err;
      });
    });
  });
}

concatFiles(args);
