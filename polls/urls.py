from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('hello/', views.hello_view, name='hello'),
    path('calc/', views.calc_view, name='calc'),
]
