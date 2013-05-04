define(['jquery', 'highcharts'], function() {
  var initialize = function() {
    $(function() {
      $(document).on("change", "#logs_selector", function() {
        var emitter = $(this).children("option:selected");
        var anomalies_container = $("#anomalies");
        $.get(emitter.data("anomalies"), function(data) {
          anomalies_container.html(data);
        });
      });
    });
  }

  return {
    initialize: initialize
  }
});
