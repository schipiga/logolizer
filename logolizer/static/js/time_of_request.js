define(['jquery', 'highcharts'], function() {
  var TimeRequest = function(url, container) {
    $.getJSON(url, function(data) {
      container.highcharts({
        chart: {
          zoomType: 'x',
          spacingRight: 20
        },
        plotOptions: {
          area: {
            marker: {
              enabled: false
            }
          }
        },
        series: [{
          data: data
        }]
      });
    });
  }

  return TimeRequest
});
