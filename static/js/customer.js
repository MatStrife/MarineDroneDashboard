$(document).ready(function(){
    var dataTable = $("#dataTable").DataTable()
    var customerChannel = pusher.subscribe('customer');
    customerChannel.bind('add', function(data) {
    var date = new Date();
    dataTable.row.add([
        data.type,
        data.latitude,
        data.longitude,
        data.level,
        `${date.getDay()}/${date.getMonth()}/${date.getFullYear()}`,
      ]).draw( false );
    });
  });