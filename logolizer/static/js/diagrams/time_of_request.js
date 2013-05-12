define(['jquery', 'highcharts'], function() {
  var TimeRequest = function(url, container) {
    $.getJSON(url, function(data) {
      container.highcharts({
        chart: {
          zoomType: 'x',
          spacingRight: 20
        },
        title: {
          text: "Time of Request"
        },
        plotOptions: {
          area: {
            marker: {
              enabled: false
            }
          }
        },
        series: [{
          name: "time of request",
          data: data
        }]
      });
    });
  }

  return TimeRequest
});
