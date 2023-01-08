from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCreateCarView.as_view()),
    path('<int:pk>', views.UpdateDeleteCarView.as_view()),
]
