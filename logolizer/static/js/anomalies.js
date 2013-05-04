define(['jquery', 'highcharts'], function() {
  var Anomalies = function(url, container) {
    $.get(url, function(data) {
      container.html(data);
    });
  }

  return Anomalies
});
