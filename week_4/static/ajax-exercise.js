"use strict";


// PART 1: SHOW A FORTUNE

function loadFortune(fortune) {

    $('#fortune-text').html(fortune);

}

function getFortune(evt) {

    // get the fortune

    $.get('/fortune', loadFortune);


    // TODO: get the fortune and show it in the #fortune-text div
}

$('#get-fortune-button').on('click', getFortune);



// PART 2: SHOW WEATHER

function displayWeather(result) {
    // result is a json string which JS will treat as an object
    // because it was identified as json in the headers

    $('#weather-info').html(result.forecast);

}

function showWeather(evt) {
    evt.preventDefault();

    var url = "/weather.json";

    var zipData = {'zipcode': $("#zipcode-field").val()}

    // $.get(url, zipData, displayWeather)

    $.get(url, zipData, function(result) {

        $('#weather-info').html(result.forecast);

    });

    // TODO: request weather with that URL and show the forecast in #weather-info
}

$("#weather-form").on('submit', showWeather);


// PART 3: ORDER MELONS

function orderMelons(evt) {
    evt.preventDefault();

    var melonData = {'melon_type': $('#melon-type-field').val(), 
                 'qty': $('#qty-field').val()};

    // TODO: show the result message after your form
    $.post('/order-melons.json', melonData, function(result) {

        // Show the result text in the #order-status div.

        $('#order-status').html(result.msg);

    });


    // TODO: if the result code is ERROR, make it show up in red (see our CSS!)
}

$("#order-form").on('submit', orderMelons);


