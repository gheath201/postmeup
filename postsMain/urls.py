from django.urls import path

from . import views



urlpatterns = [

    path("<int:pk>/", views.post, name="post"),

]