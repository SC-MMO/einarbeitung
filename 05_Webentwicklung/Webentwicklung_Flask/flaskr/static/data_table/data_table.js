$(document).ready(function () {
  $('#dataTable').DataTable({
    pagingType: 'full_numbers',
    language: {
      search: "Search: ",
      paginate: {
        first: '<<',
        previous: '<',
        next: '>',
        last: '>>'
      },
      info: "Showing _START_ to _END_ of _TOTAL_ entries",
      infoFiltered: "(filtered from _MAX_)"
    }
  });
});