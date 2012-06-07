# -*- coding: utf-8 -*
from random import choice, shuffle
from django.db import models

class BiasedManager(models.Manager):
	def by_time(self, **kwargs):
		all = super(BiasedManager, self).get_query_set().filter(**kwargs)
		result = []
		for i in all:
			for j in range(i.often):
				result.append(i)
		return result
	
	def one(self, **kwargs):
		return choice(self.by_time(**kwargs))
	
	def by_often(self, **kwargs):
		result = self.by_time(**kwargs)
		shuffle(result)
		return result
