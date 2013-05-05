define(['jquery',
        'status_count',
        'top',
        'time_of_request',
        'anomalies'], function(jQuery,
                               StatusCount,
                               Top,
                               TimeRequest,
                               Anomalies) {

  var initialize = function() {
    $(function() {
      $(document).on("click", ".log_selector", function() {
        new StatusCount($(this).data("status"), $("#status_count"));
        new TimeRequest($(this).data("time"), $("#time_of_request"));
        new Top($(this).data("top"), $("#top"));
        new Anomalies($(this).data("anomalies"), $("#anomalies"));
 
        $('.container').show();
        
        $('.log_selector').removeClass('active');
        $(this).addClass('active');
      });

      $(document).on("click", ".hide", function(event) {
        event.preventDefault();
        $(this).siblings('div').toggle();
      });
    });
  }

  return {
    initialize: initialize
  }
});
