Подключение:
1)	Добавить 'banner' в INSTALLED_APPS в settings.py
2)	Добавить url(r'^banner/', include('banner.urls')) в urls.py

Улучшения:
1) model.py
	0) коментарии
2) admin.py
	0) коментарии
	1) графики и зделать красиво
3) managers.py
	0) коментарии
4) templatetags/banners.py
	{{ banner 'slider' 'one' 'slider.html'}}
	0) коментарии
5) шаблоны вывода
	0) коментарии
	1) для слайдера
	2) слайдер банеров
	3) один банер
6) static

Всё хорошо:
1) views.py
	0) коментарии
2) urls.py
	0) коментарии


sudo -u rus-yurist.ru django-admin makemessages -l ru
sudo -u rus-yurist.ru django-admin compilemessages
/etc/init.d/apache2 restart
