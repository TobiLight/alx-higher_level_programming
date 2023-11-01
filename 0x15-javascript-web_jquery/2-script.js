/**
 * File: 2-script.js
 * Author: Oluwatobiloba Light
 * Updates the text color of the <header> element to red (#FF0000) when
 * 	-- the user clicks on the tag DIV#red_header
 */

const red_header = $('div#red_header');

if (red_header) {
  red_header.on('click', (event) => {
    red_header.css('color', '#FF0000');
  });
}
