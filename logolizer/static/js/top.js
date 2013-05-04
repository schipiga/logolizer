define(['jquery', 'tablesorter', 'highcharts'], function() {
  var Top = function(url, container) {
    $.get(url, function(data) {
      container.html(data);
      $("table").tablesorter();
    });
  }

  return Top
});
