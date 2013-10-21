django-banners
==============

Best banners app! Support rotation, sliders, branding, statistics!


Install
-------
* Add ```'banners',``` to INSTALLED_APPS in settings.py
* Add ```url(r'^banners/', include('banners.urls')),``` in urls.py
* manage.py syncdb
* manage.py collectstatic
* add to your head

```html
<!-- Если используется шаблон слайдера -->
<link rel="stylesheet" href="/static/banners/css/slider.css">
<script src="/static/banners/js/slider.js" type="text/javascript"></script>

<!-- Если используется сбор статистики -->
<script src="/static/banners/js/log.js" type="text/javascript"></script>
```


Required
--------
* jQuery - http://jquery.com/
* sorl-thumbnail https://github.com/sorl/sorl-thumbnail


How to use
----------
```html
{% load banner %}
{% banner_group 'group_name' ['slider.html'] %}
```


Documentation
-------------
https://django-banners.readthedocs.org/ru/latest/


Todo
----
* Add new templates for sliders
* Fix log.js
* Add graph and statistic to admin or custom page

* Add to banners
	* ? Count to show limit
	* ? Count to click limit
	* ? Only one show per user limit
	* ? Only one click per user limit
