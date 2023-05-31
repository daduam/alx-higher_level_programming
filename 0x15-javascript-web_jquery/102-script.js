$(function () {
  $('input#btn_translate').on('click', function () {
    const code = $('input#language_code').val();
    if (code !== '') {
      $.getJSON(
        `https://hellosalut.stefanbohacek.dev/?lang=${code}`,
        function (translation) {
          $('div#hello').text(translation.hello);
        }
      );
    }
  });
});
