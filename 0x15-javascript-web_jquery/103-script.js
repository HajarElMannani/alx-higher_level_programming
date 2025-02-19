document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').click(function () {
    translation();
  });
  $('#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      translation();
    }
  });
  function translation () {
    const value = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + value, function (data) {
      $('#hello').text(data.hello);
    });
  }
});
