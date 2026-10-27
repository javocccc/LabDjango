from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    # ... tus rutas anteriores (ej. la de 'home') ...
    path('mi-cv/', views.cv_personal, name='mi_cv'),
]

urlpatterns = [
    path("", views.home, name="home"),
    path("cv/ejemplo/", views.cv_ejemplo, name="cv_ejemplo"),
]