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
        const ticketButtonHtml = `<button class="ticket-button">${ticketId}</button>`;
        const ticketDataHtml = generateTicketDataHtml(data);

        return `
            <div class="dropdown">
                ${ticketButtonHtml}
                <div class="ticket-data">${ticketDataHtml}</div>
            </div>
        `;
    }

    // Function to generate ticket data HTML
    function generateTicketDataHtml(data) {
        const excludedKeys = ['_id', 'ticket_id'];
        return Object.keys(data)
            .filter(key => !excludedKeys.includes(key))
            .map(key => `<p><strong>${key}:</strong> ${data[key]}</p>`)
            .join('');
    }
});