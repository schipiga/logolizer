require.config({
  paths: {
    highcharts: 'highchars/highcharts',
    exporting: 'highchars/modules/exporting',
    tablesorter: 'jquery.tablesorter.min',
    jquery: 'jquery-2.0.0.min'
  }
});

require(['addiction',
         'status_count',
         'top',
         'time_of_request',
         'anomalies'], function(Addiction,
                                StatusCount,
                                Top,
                                TimeRequest,
                                Anomalies) {
  Addiction.request();
  StatusCount.initialize();
  Top.initialize();
  TimeRequest.initialize();
  Anomalies.initialize();
});
