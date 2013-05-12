define(['jquery', 'highcharts'], function() {
  var HitsPerSec = function(url, container) {
    $.getJSON(url, function(data) {
      container.highcharts({
        chart: {
          type: 'spline'
        },
        title: {
          text: "Hits per Second"
        },
        series: [{
          name: 'Hits per second',
          data: data
        }]
      });
    });
  }

  return HitsPerSec
});
