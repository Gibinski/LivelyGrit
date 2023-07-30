$(document).ready(function() {
    // Function to load dynamic text from motivational_quotes.txt
    function loadDynamicText() {
        $.get('/static/motivational_quotes.txt', function(data) {
            var quotes = data.split('\n');
            var randomIndex = Math.floor(Math.random() * quotes.length);
            var randomQuote = quotes[randomIndex];
            $('#dynamic-text p').text(randomQuote);
        });
    }

    loadDynamicText(); // Load dynamic text on page load
});
