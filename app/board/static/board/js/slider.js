var rangeValues =
{
    "1": "a few",
    "2": "normal",
    "3": "a lot",
    "4": "very a lot",
    "5": "very very a lot",
    "6": "really?",
    "7": "...",
};


$(function () {
    $('#rangeText').text(rangeValues[$('#rangeInput').val()]);
    $('#rangeInput').on('input change', function () {
        $('#rangeText').text(rangeValues[$(this).val()]);
    });

});
