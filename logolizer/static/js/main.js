require.config({
  paths: {
    highcharts: 'highchars/highcharts',
    exporting: 'highchars/modules/exporting',
    tablesorter: 'jquery.tablesorter.min',
    jquery: 'jquery-2.0.0.min',
    bootstrap: 'bootstrap.min',
    top: 'diagrams/top',
    status_count: 'diagrams/status_count',
    time_of_request: 'diagrams/time_of_request',
    hits_per_sec: 'diagrams/hits_per_sec',
    anomalies: 'diagrams/anomalies'
  }
});

require(['addiction',
         'log',
         'jquery',
         'bootstrap'], function(Addiction,
                                Log) {
  Addiction.request();
  Log.initialize();

  $(document).on("submit", "#upload form", function(){
    $("#preloader_back").show();
  });
});
