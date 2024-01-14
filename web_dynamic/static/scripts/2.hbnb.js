$(document).ready(function() {
    const apiUrl = 'http://0.0.0.0:5001/api/v1/status/';
    const apiStatusElement = $('#api_status');

    // Function to update the API status
    function updateApiStatus() {
        $.get(apiUrl, function(data) {
            if (data.status === 'OK') {
                // If status is "OK", add the class "available"
                apiStatusElement.addClass('available');
            } else {
                // If status is not "OK", remove the class "available"
                apiStatusElement.removeClass('available');
            }
        });
    }

    // Initial API status check on page load
    updateApiStatus();

    // Set interval to check API status every 5000 milliseconds (5 seconds)
    //setInterval(updateApiStatus, 5000);
});
