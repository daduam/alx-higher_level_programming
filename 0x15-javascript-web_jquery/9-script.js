$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (resp) {
  $('div#hello').text(resp.hello);
});
