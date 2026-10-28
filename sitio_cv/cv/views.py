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

    def cv_javier(request):
    contexto = {
        "nombre": "Javier Carrasco",
        "titulo": "Ingeniero civil en computación e informática",
        "perfil": "Estudiante de Ingeniería Civil en Computación e Informática en la Universidad central.",
        "contacto": {
            "email": "javo7789@gmail.com",  
            "telefono": "+56956083862",  
            "ubicacion": "Chile",
        },
        "experiencia": [
            {
                "cargo": "Practicante en desarrollo de software",
                "empresa": "Mercado huerto y jardin",
                "periodo": "10/08/2026 - 10/11/2026",
                "descripcion": "Crear sitio web",
            },
        ],
        "educacion": [
            {
                "titulo": "Ingeniería Civil en Computación e Informática",
                "institucion": "Universidad Central",
                "periodo": "2022 - 2026",
                "descripcion": "Estudiante de Ingeniería Civil en Computación e Informática.",
            },
        ],
    }
    return render(request, "cv/cv_javier.html", contexto)