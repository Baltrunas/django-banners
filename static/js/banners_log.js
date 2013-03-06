
$(document).ready(function() {
	$('.b-banner-click').on('click', function(){
		$.get($(this).data('url'));
	});

	$(".b-banner").on('load', function() {
		// alert($($(this)));
		// alert($(this).data('image'));
		// alert($(this).data('view'));
		$.get($(this).data('view'));
	});


// $("img.b-banner").on('load', function() {
//   alert($(this));
// }).each(function() {
//   if(this.complete) $(this).load();
// });



	// $('.b-banner-load').ready(function(){
		// console.log($(this));
		// $.get($(this).data('image'));
	// });
});
