
$(document).ready(function() {
	$('.b-banner-click').on('click', function(){
		$.get($(this).data('url'));
	});

	$(".b-banner").on('load', function() {
		$.get($(this).data('view'));
	});
});
