document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').click(function () {
    const value = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + value, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
