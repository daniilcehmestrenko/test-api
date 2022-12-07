from rest_framework.serializers import CurrentUserDefault, HiddenField
from rest_framework import serializers

from .models import Allergen, Carrier, Category, MyAllergy


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AllergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergen
        fields = '__all__'


class CarrierSerializer(serializers.ModelSerializer):
    allergen = AllergenSerializer()
    category = CategorySerializer()

    class Meta:
        model = Carrier
        fields = '__all__'


class MyAllergySerializer(serializers.ModelSerializer):
    user = HiddenField(
            default=CurrentUserDefault()
        )
    carriers = CarrierSerializer(many=True)

    class Meta:
        model = MyAllergy
        fields = '__all__'
