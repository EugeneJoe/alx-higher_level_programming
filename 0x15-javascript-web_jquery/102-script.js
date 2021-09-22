$(document).ready(function () {
  $('#btn_translate').click(function () {
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      type: 'GET',
      data: {
        lang: $('#language_code').val()
      },
      dataType: 'jsonp',
      success: function (hello) {
        $('#hello').text(hello.hello);
      }
    });
  });
});
