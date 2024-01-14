$(document).ready(function() {
    const apiUrl = 'http://0.0.0.0:5001/api/v1/places_search/';
    const placesSection = $('.places');

    // Function to load places dynamically from the API
    function loadPlaces() {
        // Send a POST request to the API endpoint
        $.ajax({
            type: 'POST',
            url: apiUrl,
            contentType: 'application/json',
            data: JSON.stringify({}),
            success: function(data) {
                // Clear existing content in the places section
                placesSection.empty();

                // Loop through the result and create article tags representing places
                data.forEach(function(place) {
                    const article = $('<article></article>');

                    // Customize this part based on your place object structure
                    // For example, assuming each place has a 'name' property
                    const placeName = $('<h2></h2>').text(place.name);
                    article.append(placeName);

                    // Add more details as needed

                    // Append the article to the places section
                    placesSection.append(article);
                });
            },
            error: function(error) {
                console.error('Error loading places:', error);
            }
        });
    }

    // Initial load of places on page load
    loadPlaces();

    // Set interval to reload places every 5000 milliseconds (5 seconds)
    setInterval(loadPlaces, 5000);
});
