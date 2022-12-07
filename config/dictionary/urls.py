from django.urls import path

from .views import MyAllergyView


urlpatterns = [
        path(
            '',
            MyAllergyView.as_view(),
            name='my_allergy'
        ),
    ]
