from django.urls import path

from .views import (CarrierDetailAPI, CategoryListAPIView, MyAllergyListAPIView,
                    MyAllergyDetailAPIView, CarriersListAPIView)


urlpatterns = [
        path(
            '',
            MyAllergyListAPIView.as_view(),
            name='my_allergy_list'
        ),
        path(
            '<int:pk>/',
            MyAllergyDetailAPIView.as_view(),
            name='my_allergy'
        ),
        path(
            'category/',
            CategoryListAPIView.as_view(),
            name='category_list'
        ),
        path(
            'category/<int:category_pk>/',
            CarriersListAPIView.as_view(),
            name='carriers_by_category'
        ),
        path(
            'carrier/<int:pk>/',
            CarrierDetailAPI.as_view(),
            name='carrier'
        )
    ]
