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
      }
    }
  });
});
