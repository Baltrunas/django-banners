Установка
=========

* Скопируйте или склонируйте проект в папку ``banners`` в пределах области видимости
* Добавьте ``url(r'^banners/', include('banners.urls')),`` в файл urls.py
* Добавьте ``'banners',`` в INSTALLED_APPS файла settings.py
* Синхронизируйте базу данных командой ``manage.py syncdb``
* Соберите статику ``manage.py collectstatic``
* При необходимости подключите стили и скрипты модуля (вставив нижеприведённые код между тегами ``<head></head>``)

.. code-block:: html

    <!-- Если используется шаблон слайдера -->
    <link rel="stylesheet" href="/static/banners/css/slider.css">
    <script src="/static/banners/js/slider.js" type="text/javascript"></script>

    <!-- Если используется сбор статистики -->
    <script src="/static/banners/js/banners_log.js" type="text/javascript"></script>

* Альтернативно стили и скрипты можно подключить следующим образом:

.. code-block:: html

    {% load staticfiles %}
    <!-- Если используется шаблон слайдера -->
    <link href="{%  static "banners/css/slider.css" %}" rel="stylesheet" type="text/css">

    <!-- Если используется сбор статистики -->
    <script src="{% static "banners/js/slider.js" %}" type="text/javascript"></script>
    <script src="{% static "banners/js/banners_log.js" %}" type="text/javascript"></script>


