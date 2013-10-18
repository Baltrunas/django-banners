Установка
=========

* Скопируйте или склонируйте проект в папку ``banners`` в пределах области видимости
* Добавить ``'banners',`` в INSTALLED_APPS файла settings.py
* Добавить ``url(r'^banners/', include('banners.urls')),`` в файле urls.py
* Синхронизировать базу данных командой ``manage.py syncdb``
* Собрать статику ``manage.py collectstatic``
* При необходимости подключить стили и скрипты модуля (вставив нижеприведённые код между тегами ``<head></head>``)

.. code-block:: html
    <!-- Если используется шаблон слайдера -->
    <link rel="stylesheet" href="/static/css/slider.css">
    <script src="/static/js/slider.js" type="text/javascript"></script>

    <!-- Если используется сбор статистики -->
    <script src="/static/js/banners_log.js" type="text/javascript"></script>
