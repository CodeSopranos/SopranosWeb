var rangeValues =
{
    "1": "less",
    "2": "normal",
    "3": "a lot",
};


$(function () {

    // on page load, set the text of the label based the value of the range
    $('#rangeText').text(rangeValues[$('#rangeInput').val()]);

    // setup an event handler to set the text when the range value is dragged (see event for input) or changed (see event for change)
    $('#rangeInput').on('input change', function () {
        $('#rangeText').text(rangeValues[$(this).val()]);
    });

});
