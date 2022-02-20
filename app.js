"use strict";

const API_URL = "./Example_Response.json";

async function createChartAndTable() {
  let ResponseFromAPI = await fetch(API_URL);
  let JSON_Res = await ResponseFromAPI.json();
  let JSON_Data1 = JSON.parse(JSON_Res.output.data);
  let YAxis = JSON_Data1.map(JD1 => JD1['Balance at End'])
  let XAxis = YAxis.length;
  XAxis = [...Array(XAxis).keys()];

  // Define chart properties
  const labels = XAxis; // Adding X labels
  const Init_Invest_Amount = JSON_Data1[0]["Balance at Begin"];
  const Title_Label = `Balance with an Initial Investment of ${commaFormatted(Init_Invest_Amount)}`
  const data = {
    labels: labels, // Setting values for the X-Axis
    datasets: [
      {
        label: [Title_Label], // Serves as 'title' for the chart
        fill: true,
        backgroundColor: "rgb(255, 99, 132, 0.2)",
        borderColor: "rgb(255, 99, 132)",
        data: YAxis, // Setting graph values for the Y-Axis
        fill: true,
      },
    ],
  };
  const config = {
    type: "line",
    data: data,
    options: {
      plugins: {
        tooltip: { // Customize tooltip
          callbacks: {
            title: (context)=> {
              var title_string = 'Year: '+ context[0]['label'];
              return title_string;
            },
            label: (context)=> {
              var label_string = 'Balance: '+ context['formattedValue'];
              return label_string;
            }            
          },
        }
      },
      scales: {
        y: { // adds a label for Y axis
          title: {
            display: true,
            text: "← Balance →",
            color: "#ff6384",
          },
        },
        x: { // adds a label for X axis
          title: {
            display: true,
            text: "← Years →",
            color: "#ff6384",
          },
        },
      },
    },
  };

  // Setting table data
  let headers = ['Year', 'Month', 'Balance at Begin', 'Withdrawal', 'Interest Earned', 'Balance at End'];
  let tableRows = JSON_Data1
  let table = document.createElement('table');
  let headerRow = document.createElement('tr');

  // Capturing button elements
  let btnGet = document.querySelector('button');
  let myTable = document.querySelector('#table');

  /* ADDING CHART AND TABLE */
  // Get results on Click event
  btnGet.addEventListener('click', () => {
    
    // Add Chart description
    document.getElementById('accrBal').textContent = 'Accrued balance factoring interest rates, inflation and expenditure'
    // Add Chart
    const myChart = new Chart(document.getElementById("myChart"), config);
    
    /* Adding table */
    // Add Table description
    document.getElementById('yearlySpread').textContent = 'The detailed monthly spread'
    // Adding headers
    headers.forEach(headerText => {
        let header = document.createElement('th');
        let textNode = document.createTextNode(headerText);
        header.appendChild(textNode);
        headerRow.appendChild(header);
    });
    table.appendChild(headerRow);
    // Adding rows
    tableRows.forEach(emp => {
        let row = document.createElement('tr');
        Object.values(emp).forEach(text => {
            let cell = document.createElement('td');
            let textNode = document.createTextNode(text);
            cell.appendChild(textNode);
            row.appendChild(cell);
        })
        table.appendChild(row);
    });
    myTable.appendChild(table);
    // Centering the table
    document.querySelector("table").style.margin = "auto";
  });

}
createChartAndTable();

function commaFormatted(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
