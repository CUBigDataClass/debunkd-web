
  Highcharts.chart('timechart', {
        chart: {
            zoomType: 'x',
            backgroundColor: '#337bb8',
            style: {
                color: 'white',
                font: 'Montserrat'
            }
        },
        credits: {
          enabled: false
        },
        title: {
          style: {
              color: 'white',
              font: 'Montserrat'
          },
          text: 'Topic popularity over time'
        },
        xAxis: {
            type: 'datetime',
            style: {
                color: 'white',
                font: 'Montserrat'
            },
            labels: {
              style: {
                  color: 'white',
                  font: 'Montserrat'
              }
            }
        },
        yAxis: {
          style: {
              color: 'white',
              font: 'Montserrat'
          },
          title: {
            style: {
                color: 'white',
                font: 'Montserrat'
            },
            text: '# of tweets'
          },
          labels: {
            style: {
                color: 'white',
                font: 'Montserrat'
            }
          }
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            area: {
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[3]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 2,
                states: {
                    hover: {
                        lineWidth: 2
                    }
                },
                style: {
                    color: 'white',
                    font: 'Montserrat'
                },
                threshold: null
            }
        },

        series: [{
            type: 'area',
            name: 'Tweet Amount',
            data: data
        }]
    });
