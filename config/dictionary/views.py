from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                        RetrieveAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated

from .models import Carrier, Category, MyAllergy
from .serializers import (CarrierSerializer, CategorySerializer,
                          MyAllergySerializer)


class CarrierDetailAPI(RetrieveAPIView):
    serializer_class = CarrierSerializer
    permission_classes = [IsAuthenticated]
    queryset = Carrier.objects.all()
    lookup_field = 'pk'



class CarriersListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CarrierSerializer

    def get_queryset(self):
        category_pk = self.kwargs.get('category_pk')

        return Carrier.objects.filter(
                category__pk=category_pk
            )


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

