from .models import Data_User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render

def index(request):
    return render(request, "formapp/index.html")

def send_data(request):

    if request.method == "POST":

        Data_User.objects.create(
            nombres     = request.POST["nombres"],
            apellidos   = request.POST["apellidos"],
            correo       = request.POST["correo"],
            ciudad      = request.POST["ciudad"],
        )

        return render(request, "formapp/index.html", {
                "message": "Datos guardados correctamente"
            })

    else:

        return render(request, "formapp/send_data.html")
