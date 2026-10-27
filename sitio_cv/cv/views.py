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

def cv_ejemplo(request):
    contexto = {
        "nombre": "Alex Ejemplo",
        "titulo": "Estudiante de Informática",
        "contacto": {
            "email": "alex@example.com",
            "telefono": "+56 9 1234 5678",
        },
        "habilidades": [
            "Python",
            "HTML y CSS",
            "Git y GitHub",
        ],
        "experiencia": [
            {
                "cargo": "Sitio web de presentación",
                "periodo": "2026",
                "descripcion": "Desarrollo de una página personal con HTML y CSS.",
            },
            {
                "cargo": "Proyecto grupal en Django",
                "periodo": "2026",
                "descripcion": "Construcción de páginas usando vistas y templates.",
            },
        ],
    }

    return render(request, "cv/cv_ejemplo.html", contexto)