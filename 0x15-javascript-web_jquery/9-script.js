$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    type: 'GET',
    success: function (data) {
      $('#hello').text(data.hello);
    }
  });
});
