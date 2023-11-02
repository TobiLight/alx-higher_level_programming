/**
 * File: 101-script.js
 * Author: Oluwatobiloba Light
 * Adds, removes and clears LI elements from a list when the user clicks
 */

// ps: you can use window.onload but since we're using jquery, it makes sense
// to use the below...t for thanks
$(document).ready(() => {
  const add_item = $('div#add_item');
  const remove_item = $('div#remove_item');
  const clear_list = $('div#clear_list');

  // add item
  add_item.on('click', () => {
    $('ul.my_list').append('<li>Item</li>');
  });

  // remove item
  remove_item.on('click', () => {
    $('ul.my_list li:last-child').remove();
  });

  // clear the item list
  clear_list.on('click', () => {
    $('li').remove();
  });
});
