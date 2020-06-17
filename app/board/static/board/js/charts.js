var values = [], keys = [];
anychart.onDocumentReady(function () {
    var data = [];
    // create data
    for (i = 0; i < keys.length; i = i + 1) {
        data.push({x: keys[i], value: values[i]});
    }

    // create a chart and set the data
    var chart = anychart.tagCloud(data);

    // set the chart title
    chart.title("Word cloud");

    // set the container id
    chart.container("Wordcloud");

    // initiate drawing the chart
    chart.draw();

    // add an event listener to open a url on click
    chart.listen("pointClick", function(e){
    var url = "//en.wiktionary.org/wiki/" + e.point.get("x");
    window.open(url, "_blank");
    });

});

function freqChart(data) {
    var decodeHTML = function (html) {
        var txt = document.createElement('textarea');
        txt.innerHTML = html;
        return txt.value;
    };

    var string = JSON.parse(decodeHTML(JSON.stringify(data)));
    var freqAnalysis = string.slice(1,-1).split(",");
    var ind = Object.keys(freqAnalysis);
    for (k in ind) {
      values.push(freqAnalysis[k].replace(/[^0-9]/gi, ''));
      keys.push(freqAnalysis[k].replace(/[^а-яa-zA-ZА-ЯёЁ]/gi, ''));
    }
};