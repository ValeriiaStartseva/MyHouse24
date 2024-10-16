from django.shortcuts import render


def index(request):
    return render(request, "admin/adminlte_base.html")
