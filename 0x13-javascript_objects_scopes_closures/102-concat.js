#!/usr/bin/node
/**
 * File: 102-concat.js
 * Author: Oluwatobiloba Light
 * Description: Concats 2 files.
 */

const fs = require('fs');
const args = process.argv.slice(2);

function concatFiles (arg) {
  if (!args.length) return;
  const fileA = fs.readFileSync(args[0], 'utf-8');
  const fileB = fs.readFileSync(args[1], 'utf-8');
  fs.writeFileSync(args[2], fileA + '\n' + fileB + '\n');
  fs.writeFileSync(args[2], fileA + '\n' + fileB + '\n');
}

concatFiles(args);
