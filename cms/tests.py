"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


from django_any import any_model

class TestMyShop(TestCase):
    def test_order_updates_user_account(self):
        account = any_model(Pages, amount=25)
        # order = any_model(Order, user=account.user, amount=10)
        # order.proceed()

        # account = Account.objects.get(pk=account.pk)
        # self.assertEquals(15, account.amount)