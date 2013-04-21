define(['jquery-2.0.0.min'], function(jQuery) {
  var initialize = function() {
    $(function() {
      $(document).on("change", "#logs_selector", function() {
        var emitter = $(this).children("option:selected");
        var status_count = $('#status_count');
        $.get(emitter.data('url'), function(data) {
          status_count.html(data);
        });
      });
    });
  }

  return {
    initialize: initialize
  }
});
