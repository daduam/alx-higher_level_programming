$(function () {
  function getTranslation () {
    const code = $('input#language_code').val();
    if (code !== '') {
      $.getJSON(
        `https://hellosalut.stefanbohacek.dev/?lang=${code}`,
        function (translation) {
          $('div#hello').text(translation.hello);
        }
      );
    }
  }

  $('input#btn_translate').on('click', getTranslation);
  $('input#language_code').on('keypress', function (event) {
    if (event.keyCode === 13) getTranslation();
  });
});
