$(document).ready(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    type: 'GET',
    dataType: 'jsonp',
    success: function (data) {
      $('#hello').text(data.hello);
    }
  });
});
