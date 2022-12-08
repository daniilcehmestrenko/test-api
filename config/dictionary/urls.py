from django.urls import path

from .views import MyAllergyListView, MyAllergyDetailView


urlpatterns = [
        path(
            '',
            MyAllergyListView.as_view(),
            name='my_allergy_list'
        ),
        path(
            '<int:pk>/',
            MyAllergyDetailView.as_view(),
            name='my_allergy'
        ),
    ]
