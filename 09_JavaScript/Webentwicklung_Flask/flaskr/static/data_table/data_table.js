function createTableHead(table, data) {
  const thead = document.createElement("thead");
  const headerRow = document.createElement("tr");

  data.forEach(item => {
    const th = document.createElement("th");
    th.textContent = item;
    headerRow.appendChild(th);
  });

  thead.appendChild(headerRow);
  table.appendChild(thead);
  return table;
}

function createTableBody(table, data) {
  const tbody = document.createElement("tbody");

  data.forEach(row => {
    const dataRow = document.createElement("tr");
    row.forEach(cell => {
      const td = document.createElement("td");
      td.innerHTML = cell;
      dataRow.appendChild(td);
    });
    tbody.appendChild(dataRow);
  });

  table.appendChild(tbody);
  return table;
}

function loadTable(count, page_) {
  
  page = page_
  $.ajax({
    url: './test',
    method: 'GET',
    dataType: 'json',
    success: function (response) {
      const data = response;
      const objectTable = document.getElementById("objectTable");
      objectTable.innerHTML = "";
      let table = document.createElement("table");
      table.className = "display";

      table = createTableHead(table, data[0]);

      const start = (page - 1) * count;
      const end = page * count;
      page_count = Math.ceil(data[1].length / count);
      table = createTableBody(table, data[1].slice(start, end));

      objectTable.appendChild(table);
      build_pagination_pages()
    }
  });
}

var count_val = document.getElementById('entrycount').value;
var page = 1;
var page_count;

$(document).ready(function () {
  reloadTable(count_val, 1)
});

function reloadTable(count, page_=1 ) {
  count_val = count;
  page = page_
  loadTable(count_val, page)
}

function first_page() {
  if (page!=1) {
    page = 1;
    reloadTable(count_val, page)
  }
}

function previous_page() {
  if (page>1) {
    page-=1
    reloadTable(count_val, page)
  }
}

function build_pagination_pages() {  
  const container = document.getElementById('pageButtonContainer');
  container.innerHTML = "";
  let paginationPages = Array.from({length: page_count}, (x, i) => i+1);
  
  if (page_count<= 5 | page < 3) {
    paginationPages = paginationPages.slice(0, 5);
  }
  else if (page > page_count-2) {
    paginationPages = paginationPages.slice(-5);
  }
  else {
    paginationPages = paginationPages.slice(page-3, page+2);
  }
  
  paginationPages.forEach(paginationPage => {
    const button = document.createElement('button');
    button.textContent = `${paginationPage}`;
    button.id = `btn${paginationPage}`;
    if (paginationPage == page)
      button.style = `color:red;`

    button.addEventListener('click', () => {
      reloadTable(count_val, paginationPage)
    });
    container.appendChild(button);
  });
}

function next_page() {
  if (page<page_count) {
    page+=1
    reloadTable(count_val, page)
  }
}

function last_page() {
  if (page != page_count) {
    page = page_count
    reloadTable(count_val, page)
  }
}