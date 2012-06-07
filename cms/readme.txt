Install
1) Add 'cms', to INSTALLED_APPS
2) Add 'cms.middleware.PageMiddleware', to MIDDLEWARE_CLASSES
3) Add 	url(r'^', include('cms.urls')), to urls.py
4) manage syncdb