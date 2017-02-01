from modeltranslation.translator import translator
from modeltranslation.translator import TranslationOptions

from .models import Banner


class BannerTranslationOptions(TranslationOptions):
	fields = ['title', 'alt', 'text', 'img', 'url']

translator.register(Banner, BannerTranslationOptions)
