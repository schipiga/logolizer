define(['jquery-2.0.0.min', 'highcharts'], function() {
  var initialize = function() {
    $(function() {
      $(document).on("change", "#logs_selector", function() {
        var emitter = $(this).children("option:selected");
        var status_count = $('#status_count');
        $.getJSON(emitter.data('status'), function(data) {
          status_count.highcharts({
            chart: {
              type: 'bar'
            },
            title: {
              text: "Statuses count"
            },
            series: data
          });
          status_count.prepend('<span class="close">X</span>');
        });
      });

      $(document).on("click", ".close", function() {
        $(this).parent().html("");
      });
    });
  }

  return {
    initialize: initialize
  }
});
