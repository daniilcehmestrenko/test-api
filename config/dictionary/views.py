from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                        RetrieveAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Carrier, Category, MyAllergy
from .serializers import (CarrierSerializer, CategorySerializer,
                          MyAllergySerializer)


class CarrierDetailAPI(RetrieveAPIView):
    serializer_class = CarrierSerializer
    permission_classes = [IsAuthenticated]
    queryset = Carrier.objects.all()
    lookup_field = 'pk'



class CarriersListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, category_pk):
        carriers = Carrier.objects.filter(
                category__pk=category_pk
            )
        serializer = CarrierSerializer(carriers, many=True)

        return Response(serializer.data)

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class MyAllergyListAPIView(ListCreateAPIView, UpdateModelMixin):
    serializer_class = MyAllergySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return MyAllergy.objects.filter(
                user__pk=self.request.user.pk
            )


class MyAllergyDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MyAllergySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MyAllergy.objects.filter(
                user__pk=self.request.user.pk
            )

