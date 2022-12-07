from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Animal, MyAllergy, Plant, Product
from .serializers import (AnimalSerializer, MyAllergySerializerGET,
                          MyAllergySerializerPOST, PlantSerializer,
                          ProductSerializer)


class MyAllergyView(APIView):

    def get(self, request):
        my_allergy = MyAllergy.objects.filter(
                    user__pk=request.user.pk
                )
        products = Product.objects.all()
        animals = Animal.objects.all()
        plants = Plant.objects.all()

        serializer_allergy = MyAllergySerializerGET(my_allergy, many=True)
        serializer_product = ProductSerializer(products, many=True)
        serializer_animal = AnimalSerializer(animals, many=True)
        serializer_plant = PlantSerializer(plants, many=True)

        return Response({
            'my_allergy': serializer_allergy.data,
            'products': serializer_product.data,
            'animals': serializer_animal.data,
            'plants': serializer_plant.data
        })

    def post(self, request):
        serializer = MyAllergySerializerPOST(
                data=request.data,
                context={'request': request},
            )

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        new_allergy = MyAllergy.objects.last()
        serializer = MyAllergySerializerGET(new_allergy)

        return Response(serializer.data)

