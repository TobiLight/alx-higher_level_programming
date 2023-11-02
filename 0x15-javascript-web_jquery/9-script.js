/**
 * File: 9-script.js
 * Author: Oluwatobiloba Light
 * Fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and 
 *  -- displays the value of hello from that fetch in the HTML tag DIV#hello
 */

const $ = window.$

$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', res => {
	$("div#hello").text(res.hello)
});
