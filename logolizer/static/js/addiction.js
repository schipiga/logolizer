define(['jquery-2.0.0.min'], function(){
  var request = function() {
    $(function(){
      var loaded_logs = $('#loaded_logs');
      $.get(loaded_logs.data('url'), function(data) {
        loaded_logs.html(data);
      });
    });
  };

  return {
    request: request
  };
});
