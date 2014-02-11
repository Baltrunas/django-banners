$.fn.bannersSlider = function(options) {
	$this = this;
	var settings = $.extend( {
		'auto_play': false,
		'effect': 'fade',
		'speed' : 3000
	}, options);

	$this.current = 1;
	$this.old = 1;
	$this.len = $this.find('.b-slider-list li').length;

	$this.find('.b-slider-item').hide();
	$this.find('.m-slider-item-1').show();

	$this.fadeTo = function(new_num) {
		old_num = $this.old;
		if (new_num != old_num) {
			$this.find('.m-slider-item-' + new_num).hide();
			$this.find('.m-slider-item-' + new_num).fadeIn(1000);
			$this.find('.m-slider-current').fadeOut(1000);
			$this.find('.m-slider-current').removeClass('m-slider-current');
			$this.find('.m-slider-item-' + new_num).addClass('m-slider-current');

			$this.find('.b-slider-nav-button').removeClass('m-slider-nav-current_button');

			$this.find('.b-slider-nav-button[data-slide=' + new_num + ']').addClass('m-slider-nav-current_button');
		}
	};

	$this.prev = function() {
		prev = ($this.current != 1) ? $this.current - 1 : $this.len;
		$this.old = $this.current;
		$this.current = prev;

		$this.fadeTo(prev);
	};

	$this.next = function() {
		next = ($this.current != $this.len) ? $this.current + 1 : 1;
		$this.old = $this.current;
		$this.current = next;

		$this.fadeTo(next);
	};

	$this.children('.b-slider-nav-prev').on('click', function(){
		$this.prev();
	});

	$this.children('.b-slider-nav-next').on('click', function(){
		$this.next();
	});

	$this.find('.b-slider-nav-button').on('click', function(){
		to_slide = $(this).data('slide');

		$this.old = $this.current;
		$this.current = to_slide;

		$this.fadeTo(to_slide);
	});

	if (settings.auto_play) {
		setInterval(function() {
			$this.next();
		}, settings.speed);
	}

	return $this;
};
