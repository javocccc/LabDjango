from django.shortcuts import render
from django.shortcuts import render

def cv_personal(request):
    return render(request, 'cv_personal.html')


def home(request):
    contexto = {
        "integrantes": [
            {"nombre": "Tu nombre completo", "url": "#"},
            {"nombre": "Matías", "url": "#"},
        ]
    }

    return render(request, "home.html", contexto)