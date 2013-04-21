require(['addiction', 'status_count'], function(Addiction, StatusCount) {
  Addiction.request();
  StatusCount.initialize();
});
