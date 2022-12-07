from django.contrib import admin

from .models import Allergen, Animal, MyAllergy, Plant, Product


admin.site.register(Allergen)
admin.site.register(Animal)
admin.site.register(MyAllergy)
admin.site.register(Plant)
admin.site.register(Product)
