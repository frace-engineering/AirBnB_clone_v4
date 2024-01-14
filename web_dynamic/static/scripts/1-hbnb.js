<<<<<<< HEAD
$('document').ready(function () {
  let amenities = {};
  $('INPUT[type="checkbox"]').change(function () {
    if ($(this).is(':checked')) {
      amenities[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete amenities[$(this).attr('data-id')];
    }
    $('.amenities H4').text(Object.values(amenities).join(', '));
  });
=======
$(document).ready(function() 
{
    const amenityIDs = {};
	$('input[type="checkbox"]').change(function() {
	    const amenityID = $(this).data('id');
	    const amenityNmane = $(this).data('name');

	    if ($(this).is(':checked'))
	    {
	 	amenityIDs[amenityID] = amenityID;
	    } else {
		    delete amenityIDs[amenityID];
		}

        $('.menities.popover > li').text(Object.values(amenityIDs).join(', '));
    });
	$(".popover  li").text("Yes we are here");
>>>>>>> f7ca81b5d757da9e2697dcb041c742cd287be516
});
