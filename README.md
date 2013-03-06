django-banners
=========
Best banners app! Support rotation, sliders, sttistics!


# Install
* Add ```'banners',``` to INSTALLED_APPS in settings.py
* Add ```url(r'^banners/', include('banners.urls')),``` in urls.py
* manage.py syncdb
* manage.py collectstatic
* add to your head

```html
<link rel="stylesheet" href="/static/css/slider.css">
<script src="/static/js/slider.js" type="text/javascript"></script>
```
# Required
* jQuery - http://jquery.com/
* sorl-thumbnail https://github.com/sorl/sorl-thumbnail


# Plans
=========
* Add comments to model.py
* Add comments to admin.py
* Add graph to admin
* Add comments to managers.py
* Add templatetags/banners.py ```{{ banner 'slider' 'one' 'slider.html'}}```
5) шаблоны вывода
	0) коментарии
	1) для слайдера
	2) слайдер банеров
	3) один банер
