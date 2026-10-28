from django.shortcuts import render
from django.urls import reverse


def home(request):
    contexto = {
        "integrantes": [
            {
                "nombre": "Matías Olivares",
                "url": reverse("cv_matias"),
            },
        ]
    }
    return render(request, "home.html", contexto)


def cv_matias(request):
    contexto = {
        "nombre": "Matías Olivares",
        "titulo": "Estudiante de Ingeniería Civil en Computación e Informática",
        "habilidades": [
            "Desarrollo web",
            "Programación",
            "Atención al cliente",
        ],
        "experiencia": [
            "Desarrollo de tres sitios web y software",
            "Guardia de seguridad en un pub",
            "Cajero en Doggis",
        ],
    }
    return render(request, "cv_matias.html", contexto)
