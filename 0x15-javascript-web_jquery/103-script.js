$(document).ready(function () {
  $('#btn_translate').click(() => ola());
  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      ola();
    }
  });
});

function ola () {
  $.ajax({
    url: 'https://www.fourtonfish.com/hellosalut/hello/',
    type: 'GET',
    data: {
      lang: $('#language_code').text()
    },
    success: function (hello) {
      $('#hello').text(hello.hello);
    }
  });
}
