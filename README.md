dj-banner
=========
�����������:
1)	�������� 'banner' � INSTALLED_APPS � settings.py
2)	�������� url(r'^banner/', include('banner.urls')) � urls.py

���������:
1) model.py
	0) ����������
2) admin.py
	0) ����������
	1) ������� � ������� �������
3) managers.py
	0) ����������
4) templatetags/banners.py
	{{ banner 'slider' 'one' 'slider.html'}}
	0) ����������
5) ������� ������
	0) ����������
	1) ��� ��������
	2) ������� �������
	3) ���� �����
6) static

�� ������:
1) views.py
	0) ����������
2) urls.py
	0) ����������


sudo -u rus-yurist.ru django-admin makemessages -l ru
sudo -u rus-yurist.ru django-admin compilemessages
/etc/init.d/apache2 restart
