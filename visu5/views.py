from django.shortcuts import render, get_object_or_404, redirect
from porque.models import Porque
from porque.forms import PorqueForm

# Create your views here.


def visu(request):

    datos = Porque.objects.all()
    return render(request, "visu5/visualizacion5.html", {"datos":datos})

def dashboard(request):
    return render(request, 'visu5/dashboard.html')


def editar_porque(request, pk):
    porque = get_object_or_404(Porque, pk=pk)
    if request.method == 'POST':
        form = PorqueForm(request.POST, instance=porque)
        if form.is_valid():
            form.save()
            return redirect('visu')
    else:
        form = PorqueForm(instance=porque)
    return render(request, 'visu5/editar.html', {'form': form, 'porque': porque})


def eliminar_porque(request, pk):
    porque = get_object_or_404(Porque, pk=pk)
    if request.method == 'POST':
        porque.delete()
        return redirect('visu')

