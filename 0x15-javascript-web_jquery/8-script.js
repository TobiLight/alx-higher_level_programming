/**
 * File: 8-script.js
 * Author: Oluwatobiloba Light
 * Fetches and lists the title for all movies by using this URL:
 *   -- https://swapi-api.alx-tools.com/api/films/?format=json
 */

const list_movies = $('ul#list_movies');

if (list_movies) {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: res => {
      const movies = res.results;
      for (const movie in movies) {
        const movie_title = $(`<li>${movies[movie].title}</li>`);
        list_movies.append(movie_title);
      }
    }
  });
}
