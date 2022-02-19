"use strict";

const API_URL = "./Example_Response.json";

async function createChart() {
  let ResponseFromAPI = await fetch(API_URL);
  let JSON_Res = await ResponseFromAPI.json();
  let JSON_Data1 = JSON.parse(JSON_Res.output.data1);
  let YAxis = JSON_Data1.map(({ Balance_at_End }) => ({ Balance_at_End }));
  
  // Define X and Y values
  YAxis = YAxis.map((a) => a.Balance_at_End);
  let XAxis = YAxis.length;
  XAxis = [...Array(XAxis).keys()];
  
  // Define chart properties
  const labels = XAxis; // Adding X labels
  const data = {
    labels: labels, // Setting values for the X-Axis
    datasets: [
      {
        label: "TBD_name_label", // Serves as 'title' for the chart
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
      scales: {
        y: { // adds a label for Y axis
          title: {
            display: true,
            text: "Balance",
            color: "#ff6384",
          },
        },
        x: { // adds a label for X axis
          title: {
            display: true,
            text: "Years",
            color: "#ff6384",
          },
        },
      },
    },
  };

  // Add Chart
  const myChart = new Chart(document.getElementById("myChart"), config);
}
createChart();
