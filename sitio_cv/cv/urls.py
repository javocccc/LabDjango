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
    path('cv/matias/', views.cv_matias, name='cv_matias'),
]