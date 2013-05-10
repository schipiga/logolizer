require.config({
  paths: {
    highcharts: 'highchars/highcharts',
    exporting: 'highchars/modules/exporting',
    tablesorter: 'jquery.tablesorter.min',
    jquery: 'jquery-2.0.0.min',
    bootstrap: 'bootstrap.min'
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
