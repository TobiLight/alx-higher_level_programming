/**
 * File: 7-script.js
 * Author: Oluwatobiloba Light
 * Fetches the character name from this URL: 
 * -- https://swapi-api.alx-tools.com/api/people/5/?format=json
 */

const character_name = $('div#character');

if (character_name) {
	// $.ajax("https://swapi-api.alx-tools.com/api/people/5/?format=json").done((res) => {
	// 	character_name.text(res.name)
	// })
	$.ajax({
		url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
		success: res => {
			character_name.text(res.name)
		}
	})
}
