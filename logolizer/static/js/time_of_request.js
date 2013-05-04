define(['jquery', 'highcharts'], function() {
  var initialize = function() {
    $(function() {
      $(document).on("change", "#logs_selector", function() {
        var emitter = $(this).children("option:selected");
        var time_container = $("#time_of_request");
        $.getJSON(emitter.data("time"), function(data) {
          time_container.highcharts({
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
      });
    });
  }

  return {
    initialize: initialize
  }
});
