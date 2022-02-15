
  "use strict";
  const API_URL = "./Example_Response.json"
  
  async function createChart(){
    let ResponseFromAPI = await fetch(API_URL);
    let JSON_Res = await ResponseFromAPI.json();
    let JSON_Data1 = JSON.parse(JSON_Res.output.data1);
    let YAxis = JSON_Data1.map(({ Balance_at_End }) => ({ Balance_at_End }));
    YAxis = YAxis.map(a => a.Balance_at_End);
    let XAxis = YAxis.length;
    XAxis = Array.from({length: XAxis}, (_, index) => index + 1);
    
    // Define chart properties
    const labels = XAxis; // Adding X labels
    const data = {
      labels: labels, // Setting values for the X-Axis
      datasets: [
        {
          label: "TBD_name_label", // TBD
          fill: true,
          backgroundColor: "rgb(255, 99, 132, 0.2)",
          borderColor: "rgb(255, 99, 132)",
          data: YAxis, // Setting graph values for the Y-Axis
        },
      ],
    };
    const config = {
      type: "line",
      data: data,
      options: {},
    };
    
    // Add Chart
    const myChart = new Chart(document.getElementById("myChart"), config);
  
  
  }
  createChart()
  