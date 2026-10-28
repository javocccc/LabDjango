from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cv/ejemplo/", views.cv_ejemplo, name="cv_ejemplo"),
    path("cv/fabian/", views.cv_fabian, name="cv_fabian"),
    path("mi-cv/", views.cv_personal, name="mi_cv"),
]