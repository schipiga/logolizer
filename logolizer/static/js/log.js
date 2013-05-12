define(['jquery',
        'status_count',
        'top',
        'time_of_request',
        'hits_per_sec',
        'anomalies'], function(jQuery,
                               StatusCount,
                               Top,
                               TimeRequest,
                               HitsPerSec,
                               Anomalies) {

  var initialize = function() {
    $(function() {
      $(document).on("click", ".log_selector", function() {
        new StatusCount($(this).data("status"), $("#status_count"));
        new TimeRequest($(this).data("time"), $("#time_of_request"));
        new Top($(this).data("top"), $("#top"));
        new HitsPerSec($(this).data("hits"), $("#hits_per_sec"));
        new Anomalies($(this).data("anomalies"), $("#anomalies"));
 
        $('.container').show();
        $('.log_selector').removeClass('active');
        $(this).addClass('active');
      });

      $(document).on("click", ".remove", function(event) {
        var that = $(this);
        event.preventDefault();
        that.siblings('div').toggle();
        if (that.html() === "hide") {
          that.html("show");
        }else{
          that.html("hide");
        }
      });
    });
  }

  return {
    initialize: initialize
  }
});
