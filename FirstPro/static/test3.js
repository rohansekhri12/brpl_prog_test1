document.addEventListener('DOMContentLoaded', function() {
    
  const circleDropdown = document.getElementById('circle_dropdown');
  const divisionDropdown = document.getElementById('division_dropdown');
  const subdivisionDropdown = document.getElementById('subdivision_dropdown');

  circleDropdown.addEventListener('change', function() {
      const selectedCircleId = circleDropdown.value;
      console.log(selectedCircleId)
      fetch(`/get_divisions/?circle_id=${selectedCircleId}`)
          .then(response => response.json())
          .then(data => {
              divisionDropdown.innerHTML = '';

              for (const division of data) {
                  const option = document.createElement('option');
                  option.value = division.DIVISIONNAME;
                  console.log(option.value)
                  option.textContent = division.DIVISIONNAME;
                  divisionDropdown.appendChild(option);
              }
          })
          .catch(error => console.error("Fetch error agaya bhai:(",error));
  });
  divisionDropdown.addEventListener('change', function() {
    const selectedDivisionName = divisionDropdown.value;

    // Debugging: Log the selectedDivisionName to check its value
    console.log('Selected Division Name:', selectedDivisionName);

    if (selectedDivisionName) {  // Ensure a valid division name is selected
        fetch(`/get_subdivisions/?division_name=${selectedDivisionName}`)
            .then(response => response.json())
            .then(data => {
                // Clear existing options
                subdivisionDropdown.innerHTML = '';

                // Populate the Subdivision dropdown with fetched data
                data.forEach(subdivision => {
                    const option = document.createElement('option');
                    option.value = subdivision.SUB_DIVISION_DESC;
                    option.textContent = subdivision.SUB_DIVISION_DESC;
                    subdivisionDropdown.appendChild(option);
                });
            })
            .catch(error => console.error("Fetch error:", error));
    }
});
});
    //--------------------------------------------------submit button---------------------------

    document.addEventListener("DOMContentLoaded", function () {
        document.getElementById("submitBtn").addEventListener("click", function () {
            // Collect form data
            var empId = document.getElementById("usernameInput").value;
            console.log(empId)
            var circleId = document.getElementById("circle_dropdown").value;
            var divisionId = document.getElementById("division_dropdown").value;
            var wardNo = document.getElementById("ward_id").value;
            var meetingHost = document.getElementById("host_id").value;
            var issueType = document.getElementById("issuetype_id").value;
            var brplView = document.getElementById("brplview_id").value;
            var targetDate = document.getElementById("dateInput").value;
            var subDivision = document.getElementById("subdivision_dropdown").value;
            var issueRaisedBy = document.getElementById("issueraised_id").value;
            var counselor = document.getElementById("counselor_id").value;
            var meetingDate = document.getElementById("meetingdate_id").value;
            var meetingAttendees = document.getElementById("attended_id").value;
            var description = document.getElementById("description_id").value;
            var actionPlan = document.getElementById("actionplan_id").value;
            
            // Prepare data object
            var formData = {
                empId: empId,
                circleId: circleId,
                divisionId: divisionId,
                wardNo: wardNo,
                meetingHost: meetingHost,
                issueType: issueType,
                brplView: brplView,
                targetDate: targetDate,
                subDivision: subDivision,
                issueRaisedBy: issueRaisedBy,
                counselor: counselor,
                meetingDate: meetingDate,
                meetingAttendees: meetingAttendees,
                description: description,
                actionPlan: actionPlan
            };
    
            // Send data to the server using AJAX
            $.ajax({
                type: "POST",
                url: "{% url 'upload_form/' %}",
                data: {
                    'empId': empId ,
                    'circleid': circleId , 
                    'divisionId' :divisionId ,
                    'wardno': wardNo ,
                    'meetinghost': meetingHost ,
                    'issuetype':issueType ,
                    'brplview': brplView ,
                    'targetdate':targetDate ,
                    'subdivision':subDivision ,
                    'issueraisedby':issueRaisedBy ,
                    'counselor':counselor ,
                    'meetingdate': meetingDate ,
                    'meetingattendee':meetingAttendees ,
                     'description':description ,
                     csrfmiddlewaretoken:'{{ csrf_token }}'
    
                },
                success: function (response) {
                    alert(response);  // Display a success message
                },
                error: function () {
                    alert("An error occurred.");  // Display an error message
            }
        
    }); 
});

});














   
