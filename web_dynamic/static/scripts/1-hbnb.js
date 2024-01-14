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
});
