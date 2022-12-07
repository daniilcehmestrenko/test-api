from django.contrib import admin

from .models import Allergen, Carrier, Category, MyAllergy


admin.site.register(Allergen)
admin.site.register(Carrier)
admin.site.register(Category)
admin.site.register(MyAllergy)
