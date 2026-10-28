from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cv/matias/", views.cv_matias, name="cv_matias"),
]
