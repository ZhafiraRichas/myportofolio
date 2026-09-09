from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Zhafira Richas",
        "npm": "2506540941",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Known as Fira or Ichas. Second year Computer Science student at Universitas Indonesia. "
            "Who still find out what i want to do with my life ^^, but lately i like to explore new experiences."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Zhafira Richas",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)