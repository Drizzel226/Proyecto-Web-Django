from django.shortcuts import render, get_object_or_404, redirect
from porque.models import Porque
from porque.forms import PorqueForm

# Create your views here.



def visu(request):

    datos = Porque.objects.all()
    return render(request, "visu5/visualizacion5.html", {"datos":datos})

def dashboard(request):
    return render(request, 'visu5/dashboard.html')




