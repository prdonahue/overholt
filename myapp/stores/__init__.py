# -*- coding: utf-8 -*-
"""
    myapp.stores
    ~~~~~~~~~~~~~~~

    myapp stores package
"""

from ..core import Service, MyAppError
from .models import Store


class StoresService(Service):
    __model__ = Store

    def add_manager(self, store, user):
        if user in store.managers:
            raise MyAppError(u'Manager exists')
        store.managers.append(user)
        return self.save(store), user

    def remove_manager(self, store, user):
        if user not in store.managers:
            raise MyAppError(u'Invalid manager')
        store.managers.remove(user)
        return self.save(store), user

    def add_product(self, store, product):
        if product in store.products:
            raise MyAppError(u'Product exists')
        store.products.append(product)
        return self.save(store)

    def remove_product(self, store, product):
        if product not in store.products:
            raise MyAppError(u'Invalid product')
        store.products.remove(product)
        return self.save(store)
