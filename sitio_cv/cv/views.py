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

def cv_matias(request):
    contexto = {
        'nombre': 'Matías Olivares',
        'titulo': 'Estudiante / Desarrollador',
        'contacto': 'matias@ejemplo.com',
        'habilidades': ['Python', 'Django', 'Git', 'Resolución de problemas'],
        'experiencia': ['Laboratorios de Programación de Aplicaciones (2026)']
    }
    return render(request, 'cv_matias.html', contexto)