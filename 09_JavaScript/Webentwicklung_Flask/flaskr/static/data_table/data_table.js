function filter_data(data_, filter) {
  let res = [];
  filter = filter.toLowerCase();
  data_.forEach(item => {
    if (item.some(element => String(element).toLowerCase().includes(filter)))
      res.push(item);
  });
  return res;
}

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
      let data = response;

      const objectTable = document.getElementById("objectTable");
      objectTable.innerHTML = "";
      
      let table = document.createElement("table");
      table.className = "display";

      table = createTableHead(table, data[0]);
      
      if (filter) {
        data[1] = filter_data(data[1], filter)
      }

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
var filter = ""

$(document).ready(function () {
  reloadTable(1, count_val)
});

function reloadTable(page_=1, count=count_val) {
  count_val = count;
  page = page_
  loadTable(count_val, page, filter)
}

function first_page() {
  if (page!=1) {
    page = 1;
    reloadTable(page, count_val)
  }
}

function previous_page() {
  if (page>1) {
    page-=1
    reloadTable(page, count_val)
  }
}

function handle_pagination_pages() {
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
  return paginationPages
}

function create_pagination_button(paginationPage) {
  const button = document.createElement('button');
    button.textContent = `${paginationPage}`;
    button.id = `btn${paginationPage}`;
    if (paginationPage == page)
      button.style = `color:red;`

    button.addEventListener('click', () => {
      reloadTable(paginationPage, count_val)
    });
    return button
}

function build_pagination_pages() {  
  const container = document.getElementById('pageButtonContainer');
  container.innerHTML = "";

  const paginationPages = handle_pagination_pages()
  
  paginationPages.forEach(paginationPage => {
    container.append(create_pagination_button(paginationPage))
  });
}

function next_page() {
  if (page<page_count) {
    page+=1
    reloadTable(page, count_val)
  }
}

function last_page() {
  if (page != page_count) {
    page = page_count
    reloadTable(page, count_val)
  }
}

function filter_change(newFilter) {
  filter = newFilter
  reloadTable(1, count_val)
}