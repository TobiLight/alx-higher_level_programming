/**
 * File: 4-script.js
 * Author: Oluwatobiloba Light
 * Toggles the class of the <header> element when the user clicks on the
 * tag DIV#toggle_header
 */

const toggle_header = $('div#toggle_header');

if (toggle_header) {
  toggle_header.on('click', (event) => {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red');
      $('header').addClass('green');
    } else {
      $('header').removeClass('green');
      $('header').addClass('red');
    }
  });
}
