from django.shortcuts import render
from .models import Error, Programmer, Fix


def index(request):
    errors = Error.objects.all()
    programmers = Programmer.objects.all()
    fixes = Fix.objects.all()
    return render(
        request,
        "index.html",
        {
            "errors": errors,
            "programmers": programmers,
            "fixes": fixes,
        },
    )
