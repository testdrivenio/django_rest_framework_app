# shopping_list/admin.py


from django.contrib import admin

from shopping_list.models import ShoppingItem, ShoppingList

admin.site.register(ShoppingItem)
admin.site.register(ShoppingList)
