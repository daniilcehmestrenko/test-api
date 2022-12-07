from rest_framework.generics import ListCreateAPIView

from .models import MyAllergy
from .serializers import MyAllergySerializer


class MyAllergyView(ListCreateAPIView):
    serializer_class = MyAllergySerializer
    
    def get_queryset(self):
        return MyAllergy.objects.filter(
                user__pk=self.request.user.pk
            )
