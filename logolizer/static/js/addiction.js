define(['jquery', 'tablesorter'], function(){
  var request = function() {
    $(function(){
      var loaded_logs = $('#loaded_logs');
      $.get(loaded_logs.data('url'), function(data) {
        loaded_logs.html(data);
        $("table").tablesorter();
      });
    });
  };

  return {
    request: request
  };
});
