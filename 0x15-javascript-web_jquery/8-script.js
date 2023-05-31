$.getJSON(
  'https://swapi-api.alx-tools.com/api/films/?format=json',
  function (films) {
    $.each(films.results, function (_index, film) {
      $('ul#list_movies').append(`<li>${film.title}</li>`);
    });
  }
);
