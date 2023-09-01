
$(document).ready(function() {
    const circleDropdown = $('#circleDropdown');
    const subDropdown = $('#subDropdown');

    // Define a mapping of circle names to subdivision options
    const subdivisionMappings = {
      'Circle A': ['Subdivision A1', 'Subdivision A2', 'Subdivision A3'],
      'Circle B': ['Subdivision B1', 'Subdivision B2', 'Subdivision B3']
      // Add more mappings as needed
    };

    // Event listener for changes in the circleDropdown
    circleDropdown.change(function() {
      const selectedCircle = $(this).val();
      const subdivisions = subdivisionMappings[selectedCircle];

      // Clear existing options in the subDropdown
      subDropdown.empty();

      // Add new options to the subDropdown
      subdivisions.forEach(subdivision => {
        subDropdown.append($('<option>', {
          value: subdivision,
          text: subdivision
        }));
      });
    });
});

