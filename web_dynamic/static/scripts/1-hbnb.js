$(document).ready(function() {
	let amenityIDs = [];
	$('input[type="checkbox"]').change(function() {
		const amenityID = $(this).data('id');
		const amenityNmane = $(this).data('name');

		if ($(this).prop('checked')) {
			amenityIDs.push(amenityID);
		} else {
			amenityIDs = amenityIDs.filter(id => !== amenityID);
		}

		$('#amenities-list').text(amenitIDs.join(', '))
	});
});
