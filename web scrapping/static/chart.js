var ctx1 = document.getElementById('chart')
var tickerName = tickerName;
var chartData = chartData;


// Loop through chartData to build 2 lists one just prices and one just dates
var dates = [];
var prices = [];
var maxPrice = 0;

for (i = 0; i < chartData.length; i++) {
    dates.push(chartData[i][0]);
    prices.push(chartData[i][1]);
    if (chartData[i][1] > maxPrice) {
        maxPrice = chartData[i][1];
    }
}


// graph rendering the past data for the ticker in question----------------------
    var chart = new Chart(ctx1, {
// The type of chart we want to create
type: 'line',

// The data for our dataset
data: {
    labels: dates,
    datasets: [{
        label: 'Prices' + tickerName[0],
        backgroundColor: 'green',
        borderColor: 'black',
        data: prices
    }]
},

// Configuration options go here
options: {
        title: {
        display: false,
        text: 'Historical closing prices for ' + tickerName[0],
        fontSize: 15
    },
    scales: {
        xAxes: [{
            scaleLabel: {
                display: false,
                labelString: "Last number of days",
                fontSize: 15
            }
        }],
        yAxes: [{
            ticks: {
                beginAtZero: true,
                suggestedMax: maxPrice,
            },
            scaleLabel: {
                display: false,
                labelString: "PRICES",
                fontSize: 15
            }
        }]
    },
}
});