#!/usr/bin/node
/**
 * File: 102-concat.js
 * Author: Oluwatobiloba Light
 * Description: Concats 2 files.
 */

const fs = require('fs');
const args = process.argv.slice(2);
const fileA = args[0];
const fileB = args[1];
const fileC = args[2];

if (
  fs.existsSync(fileA) &&
  fs.statSync(fileA).isFile &&
  fs.existsSync(fileB) &&
  fs.statSync(fileB).isFile &&
  fileC !== undefined
) {
  const fileAContent = fs.readFileSync(fileA);
  const fileBContent = fs.readFileSync(fileB);
  const fileCstream = fs.createWriteStream(fileC);

  fileCstream.write(fileAContent);
  fileCstream.write(fileBContent);
  fileCstream.end();
}
