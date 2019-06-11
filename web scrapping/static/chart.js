var ctx1 = document.getElementById('chart')

var chartData = chartData;




// graph rendering the past data for the station searched----------------------
    var chart1 = new Chart(ctx1, {
// The type of chart we want to create
type: 'line',

// The data for our dataset
data: {
    labels: past_x,
    datasets: [{
        label: 'Available bikes',
        backgroundColor: '#1f567c',
        borderColor: 'black',
        data: past_y
    }]
},

// Configuration options go here
options: {
        title: {
        display: true,
        text: 'Past available bikes at station number ' + graph_data_past[0][3],
        fontSize: 15
    },
    scales: {
        xAxes: [{
            scaleLabel: {
                display: true,
                labelString: "Last 24 hours",
                fontSize: 15
            }
        }],
        yAxes: [{
            ticks: {
                beginAtZero: true,
                suggestedMax: max_past,
            },
            scaleLabel: {
                display: true,
                labelString: "Available bikes",
                fontSize: 15
            }
        }]
    },
}
});