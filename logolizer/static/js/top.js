define(['jquery', 'tablesorter', 'highcharts'], function() {
  var initialize = function() {
    $(function() {
      $(document).on("change", "#logs_selector", function() {
        var emitter = $(this).children("option:selected");
        var top_container = $("#top");
        $.get(emitter.data("top"), function(data) {
          top_container.html(data);
          $("table").tablesorter();
        });
      });
    });
  }

  return {
    initialize: initialize
  }
});
