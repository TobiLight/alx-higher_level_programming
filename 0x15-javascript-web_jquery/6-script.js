/**
 * File: 6-script.js
 * Author: Oluwatobiloba Light
 * Updates the text of the <header> element to New Header!!! when the user
 * clicks on DIV#update_header
 */

const update_header = $('div#update_header');

if (update_header) {
  update_header.on('click', (event) => {
    $('header').text('New Header!!!');
  });
}
