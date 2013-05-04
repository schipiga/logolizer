require.config({
  paths: {
    highcharts: 'highchars/highcharts',
    exporting: 'highchars/modules/exporting',
    tablesorter: 'jquery.tablesorter.min',
    jquery: 'jquery-2.0.0.min'
  }
});

require(['addiction', 'log'], function(Addiction, Log) {
  Addiction.request();
  Log.initialize();
});
