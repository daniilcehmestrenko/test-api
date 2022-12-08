from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import UpdateModelMixin

from .models import MyAllergy
from .serializers import MyAllergySerializer


class MyAllergyListView(ListCreateAPIView, UpdateModelMixin):
    serializer_class = MyAllergySerializer
    
    def get_queryset(self):
        return MyAllergy.objects.filter(
                user__pk=self.request.user.pk
            )


class MyAllergyDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = MyAllergySerializer

    def get_queryset(self):
        return MyAllergy.objects.filter(
                user__pk=self.request.user.pk
            )

