

// Create the chart
Highcharts.mapChart('container', {
    chart: {
      map: 'countries/us/us-all'
    },

    title: {
      text: 'Tweet frequency by state'
    },

    mapNavigation: {
      enabled: true,
      buttonOptions: {
          verticalAlign: 'bottom'
      }
    },

    colorAxis: {
      min: 0
    },

    series: [{
      data: data,
        name: 'Tweet frequency',
        states: {
          hover: {
            color: '#BADA55'
          }
        },
        dataLabels: {
          enabled: false,
          format: '{point.name}'
        }
      }, {
        name: 'Separators',
        type: 'mapline',
        data: Highcharts.geojson(Highcharts.maps['countries/us/us-all'], 'mapline'),
        color: 'black',
        showInLegend: false,
        enableMouseTracking: false
    }]
});
