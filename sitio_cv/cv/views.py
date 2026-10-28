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


def cv_fabian(request):
    contexto = {
        "nombre": "Fabian Silva",
        "titulo": "Estudiante",
        "cargo_actual": "Practicante Colsan",
        "perfil": (
            "Estudiante enfocado en el desarrollo de software y aplicaciones web, "
            "con experiencia práctica en Colsan. Apasionado por la tecnología, "
            "el aprendizaje continuo y la resolución efectiva de problemas mediante código."
        ),
        "contacto": {
            "email": "fsilvat2000@wawaw.com",
            "telefono": "+56 9 8765 4321",
            "ubicacion": "Chile",
        },
        "experiencia": [
            {
                "cargo": "Practicante",
                "empresa": "Colsan",
                "periodo": "2026 - Presente",
                "descripcion": (
                    "Apoyo en el desarrollo y mantenimiento de sistemas, "
                    "colaboración en procesos operativos y soporte tecnológico."
                ),
            },
            {
                "cargo": "Desarrollador Web (Proyectos Académicos)",
                "empresa": "Laboratorio de Aplicaciones",
                "periodo": "2026",
                "descripcion": (
                    "Desarrollo de aplicaciones web utilizando Django, Python, "
                    "plantillas HTML/CSS y control de versiones con Git."
                ),
            },
        ],
        "educacion": [
            {
                "titulo": "Estudiante de Informática / Computación",
                "institucion": "Universidad Central de Chile",
                "periodo": "En curso",
                "descripcion": (
                    "Formación en desarrollo de software, arquitectura de sistemas, "
                    "bases de datos y trabajo colaborativo."
                ),
            },
        ],
        "habilidades": [
            "Python",
            "Django",
            "Git & GitHub",
            "HTML5 y CSS3",
            "Bases de Datos",
            "Trabajo en Equipo",
            "Resolución de Problemas",
        ],
    }

    return render(request, "cv/cv_fabian.html", contexto)