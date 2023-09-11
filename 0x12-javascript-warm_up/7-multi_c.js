#!/usr/bin/node
/**
 * File: 7-multi.js
 * Author: Oluwatobiloba Light
 */
const arg = process.argv.slice(2);
if (!arg.length) {
	console.log('Missing number of occurrences');
}
if (arg > 0) {
	for (let i = 0; i < arg; i++) {
		console.log('C is fun');
	}
}
