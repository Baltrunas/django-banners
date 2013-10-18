django-banners
=========
Best banners app! Support rotation, sliders, branding, statistics!

# Install
* Add ```'banners',``` to INSTALLED_APPS in settings.py
* Add ```url(r'^banners/', include('banners.urls')),``` in urls.py
* manage.py syncdb
* manage.py collectstatic
* add to your head

```html
<link rel="stylesheet" href="/static/css/slider.css">
<script src="/static/js/slider.js" type="text/javascript"></script>
<script src="/static/js/banners_log.js" type="text/javascript"></script>
```

# Required
* jQuery - http://jquery.com/
* sorl-thumbnail https://github.com/sorl/sorl-thumbnail


# How to use
```html
{% load banner %}
{% banner_group 'group_name' ['slider.html'] %}
```

# Documentation
https://django-banners.readthedocs.org/ru/latest/


# Todo
* New slider types
	* Set size
	* Стрелки по бокам
		* Eнот
		* Fashion
	* Стрелки снизу с цифрами [блога енот]
* Add graph and statistic to admin or custom page
* Add template tags
	* Slider
	* Branding with rotation
	* Block load rotation
	* Block slider rotation
	* One banner

# May be
* Add to banners
	* Count to show
	* Count to click
	* Only one show
	* Only one click
* Add to group
	* Second width and height
	* Type
	* Template
