/**
 * File: 3-script.js
 * Author: Oluwatobiloba Light
 * Adds the class red to the <header> element when the user clicks on the
 * tag DIV#red_header
 */

const red_header = $('div#red_header');

if (red_header) {
	red_header.on('click', (event) => {
		$('header').addClass("red");
	});
}
