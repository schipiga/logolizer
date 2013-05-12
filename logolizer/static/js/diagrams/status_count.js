define(['jquery', 'highcharts'], function() {
  var StatusCount = function(url, container) {
    $.getJSON(url, function(data) {
      container.highcharts({
        chart: {
          type: 'bar'
        },
        title: {
          text: "Statuses count"
        },
        series: data
      });
    });
  }

  return StatusCount
});
