# -*- coding: utf-8 -*
from cms.models import *
from menu.models import *

context = {
	'test' : 'Любая корпорация добра, рано или поздно становится корпорацией бабла.<br><strong>Сколько заплатишь, на столько и получишь.</strong>',
	'top_menu' : Menu.objects.filter(public=True, parent=None, group__type='top_menu'),
}