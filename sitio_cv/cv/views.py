from django.shortcuts import render


def home(request):
    contexto = {
        "integrantes": [
            {"nombre": "Tu nombre completo", "url": "#"},
            {"nombre": "Matías", "url": "#"},
        ]
    }

    return render(request, "home.html", contexto)