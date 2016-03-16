django-banners
==============

Simple banners for django!


Install
-------
* Add ```'apps.banners',``` to INSTALLED_APPS in settings.py
* manage.py migrate banners


Required
--------
* sorl-thumbnail https://github.com/sorl/sorl-thumbnail


How to use
----------
```html
{% load banners %}
{% banners 'group_slug' ['banners/default.html'] %}
```


Documentation
-------------
https://django-banners.readthedocs.org/ru/latest/


Todo
----
* Optimize models, tags, templates


Ideas
-----
* Logs and statistic
* Count to show limit
* Count to click limit
* Only one show per user limit
* Only one click per user limit
