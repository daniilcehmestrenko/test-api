from rest_framework.serializers import (CharField, CurrentUserDefault, IntegerField,
                                        ModelSerializer, HiddenField, Serializer,
                                        ListField)

from .models import Allergen, Animal, MyAllergy, Plant, Product


class AllergenSerializer(ModelSerializer):
    class Meta:
        model = Allergen
        fields = '__all__'


class AnimalSerializer(ModelSerializer):
    allergens = AllergenSerializer(many=True)

    class Meta:
        model = Animal
        fields = '__all__'


class PlantSerializer(ModelSerializer):
    allergens = AllergenSerializer(many=True)

    class Meta:
        model = Plant
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    allergens = AllergenSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

class MyAllergySerializerPOST(Serializer):
    user = HiddenField(
            default=CurrentUserDefault()
        )
    name = CharField(
            max_length=100
        )
    user_products = ListField(
            child=IntegerField(),
            allow_empty=True
        )
    user_animals = ListField(
            child=IntegerField(),
            allow_empty=True
        )
    user_plants = ListField(
            child=IntegerField(),
            allow_empty=True
        )

    def __create_obj_lst(self, model, list_id):
        return [model.objects.get(pk=pk) for pk in list_id]
    
    def create(self, validated_data):
        my_allergy = MyAllergy.objects.create(
                    name=validated_data["name"],
                    user=validated_data['user'],
                )
        if validated_data["user_products"]:
            object_list = self.__create_obj_lst(
                    Product,
                    validated_data['user_products']
                )
            for obj in object_list:
                my_allergy.user_products.add(obj)

        if validated_data["user_animals"]:
            object_list = self.__create_obj_lst(
                    Animal,
                    validated_data['user_animals']
                )
            for obj in object_list:
                my_allergy.user_animals.add(obj)

        if validated_data["user_plants"]:
            object_list = self.__create_obj_lst(
                    Plant,
                    validated_data['user_plants']
                )
            for obj in object_list:
                my_allergy.user_plants.add(obj)
        
        return my_allergy
    

class MyAllergySerializerGET(ModelSerializer):
    user_products = ProductSerializer(
            many=True,
        )
    user_animals = AnimalSerializer(
            many=True,
        )
    user_plants = PlantSerializer(
            many=True,
        )

    class Meta:
        model = MyAllergy
        fields = (
        'name', 'user', 'user_products',
        'user_animals', 'user_plants',
    )
