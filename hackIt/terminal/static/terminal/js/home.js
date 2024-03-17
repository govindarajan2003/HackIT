$(document).ready(function(){
    // Function to fetch and display data asynchronously
    function fetchData() {
        $.ajax({
            type: "GET",
            url: "{% url 'receive_data' %}",
            success: function(response){
                // Clear previous data
                $('#result').empty();

                // Loop through each item in the response and create HTML
                $.each(response, function(index, item) {
                    var html = '<div class="result-item">';
                    html += '<p>URL: ' + item.url + '</p>';
                    html += '<p>Status: ' + item.status + '</p>';
                    html += '<button class="downloadBtn" data-id="' + item.id + '">Download</button>'; // Add a download button
                    html += '</div>';
                    $('#result').prepend(html); // Add new data on top
                });
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    }

    // Initial call to fetch data
    fetchData();

    // Set interval to fetch data every 5 seconds (for example)
    setInterval(fetchData, 5000);

    $('#submitButton').click(function(){
        var inputData = $('#inputText').val();
        $.ajax({
            type: "POST",
            url: "{% url 'send_data' %}",
            data: {
                'input_data': inputData,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response){
                // Display response message
                $('#result').html(response.message);
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });

    $('#result').on('click', '.downloadBtn', function() {
        var id = $(this).data('id');
        window.location.href = "/terminal/download/" + id;
    });

    // Function to continuously call Receiver view
    function callReceiverView() {
        $.ajax({
            type: "GET",
            url: "{% url 'receiver' %}",
            success: function(response){
                // Handle the response if needed
                console.log(response);
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    }

    // Initial call to callReceiverView function
    callReceiverView();

    // Set interval to callReceiverView every 10 seconds (for example)
    setInterval(callReceiverView, 10000);
});
