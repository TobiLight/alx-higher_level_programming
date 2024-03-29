/**
 * File: 102-script.js
 * Author: Oluwatobiloba Light
 * Fetches and prints how to say “Hello” depending on the language
 */

// ps: you can use window.onload but since we're using jquery, it makes sense
// to use the below...t for thanks
$(document).ready(() => {
  $('input#btn_translate').click(function () {
    const languageCode = $('input#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/';
    $.get(url, { lang: languageCode }, (res) => {
      $('div#hello').text(res.hello);
    });
  });
});
