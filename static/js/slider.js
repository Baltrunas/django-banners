function Slider(container){
	original_container = container;
	container = $(container + ' div').css('overflow', 'hidden').children('ul');
	imgs = container.find('img');
	console.log(imgs);
	imgWidth = imgs[0].width;
	imgsLen = imgs.length;
	current = 0;

	$(original_container).children('.slider-nav').on('click', function() {
		if ($(this).data('direction') === 'next') {
			console.log(current, imgsLen);
			if (current < imgsLen-1){
					current++;
			} else {
				current = 0;
			}
		} else if ($(this).data('direction') === 'prev') {
			if (current > 0) {
				current--;
			} else {
				current=imgsLen-1;
			}
		}
		container.animate({
			'margin-left': -( current * imgWidth )
		});
	});
}