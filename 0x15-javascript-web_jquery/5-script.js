/**
 * File: 5-script.js
 * Author: Oluwatobiloba Light
 * Adds a <li> element to a list when the user clicks on the tag DIV#add_item
 */

const li_item = $('div#add_item');

if (li_item) {
  li_item.on('click', (event) => {
    const new_item = $('<li>Item</li>');
    $('ul.my_list').append(new_item);
  });
}
