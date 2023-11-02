/**
 * File: 103-script.js
 * Author: Oluwatobiloba Light
 * Fetches and prints how to say “Hello” depending on the language
 */

// ps: you can use window.onload but since we're using jquery, it makes sense
// to use the below...t for thanks
$(document).ready(() => {
  // Function to fetch translation
  function fetchTranslation () {
    const languageCode = $('input#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/';
    $.get(url, { lang: languageCode }, (res) => {
      $('div#hello').text(res.hello);
    });
  }

  // if button is clicked
  $('input#btn_translate').click(function () {
    fetchTranslation();
  });

  // If enter button is pressed
  $('input#language_code').on('keypress', function (e) {
    // code for enter button is 13
    if (e.which === 13) {
      fetchTranslation();
    }
  });
});
