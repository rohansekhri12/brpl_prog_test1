{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="{% static '2nd_page.css' %}"/>
    <!-- Include Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Complaint Management</title>
</head>
<body>
    <div class="header">
        <img src="https://www.bsesdelhi.com/image/layout_set_logo?img_id=91257&t=1690795118097">
    </div>

    <div class="container">
        <div class="button-container">
            <button class="btn btn-danger" id="button2">Register New complaint</button>
        </div>

        <div class="frame">
            <div id="frameContent"></div>
        </div>
    </div>

    <div class="footer">
        <p>&copy; 2023 Complaint Management System. All rights reserved.</p>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const frameContent = document.getElementById('frameContent');
            const username = '{{ username|escapejs }}'; // Escape the username for JavaScript usage

            // Fetch data from the server using the username as a query parameter
            fetch(`/get_data/?emp_id=${username}`)
                .then(response => response.json())
                .then(data => {
                    const dropdownHtml = generateDropdownHtml(data);
                    frameContent.innerHTML = dropdownHtml;
                })
                .catch(error => console.error('Error fetching data:', error));

            // Function to generate dropdown HTML based on the data
            function generateDropdownHtml(data) {
                const ticketId = data.ticket_id;
                const links = Object.keys(data)
                    .filter(key => key !== '_id' && key !== 'ticket_id')
                    .map(key => `<div class="tooltip-container"><button class="tooltip-trigger">${key}</button><div class="tooltip">${data[key]}</div></div>`)
                    .join('');

                return `
                    <div class="dropdown">
                        <button class="dropbtn">${ticketId}</button>
                        <div class="dropdown-content">
                            ${links}
                        </div>
                    </div>
                `;
            }
        });
    </script>
</body>
</html>
