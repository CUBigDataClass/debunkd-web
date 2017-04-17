

// Create the chart
Highcharts.mapChart('container', {
  chart: {
    map: 'countries/us/us-all',
    backgroundColor: '#337bb8',
    style: {
        color: 'white',
        font: 'Montserrat'
    }
  },

  title: {
    text: 'Corrupted states',
    style: {
        color: 'white',
        font: 'Montserrat'
    }
  },

  legend: {
    layout: 'horizontal',
    borderWidth: 0,
    backgroundColor: 'rgba(255,255,255,0.0)',
    style: {
        color: 'white',
        font: 'Montserrat'
    },
    floating: true,
    verticalAlign: 'top',
    y: 25
  },

  mapNavigation: {
    enabled: true,
    buttonOptions: {
        verticalAlign: 'bottom'
    }
  },

  colorAxis: {
    min: 0,
    minColor: '#ffdad9',
    maxColor: '#f50000',
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
