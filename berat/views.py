from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Berat
from .forms import BeratForm
from datetime import datetime


def index(request):
    template = loader.get_template('berat/index.html')
    data = Berat.objects.order_by('tanggal')

    avg_max = 0
    avg_min = 0
    avg_diff = 0

    if len(data) > 0:
        for d in data:
            avg_max += d.berat_max
            avg_min += d.berat_min
            avg_diff += d.diff

        avg_max /= float(len(data))
        avg_min /= float(len(data))
        avg_diff /= float(len(data))
        
    context = {
    	'data': data,
    	'avg_max': avg_max,
    	'avg_min': avg_min,
    	'avg_diff': avg_diff
    }
    return HttpResponse(template.render(context, request))

def tambah(request):
    if request.method == 'POST':
        form = BeratForm(request.POST)

        if form.is_valid():
            bmax = form.cleaned_data['berat_max']
            bmin = form.cleaned_data['berat_min']
            tgl = datetime.now()
            diff = bmax-bmin

            obj = Berat()
            obj.tanggal = tgl
            obj.berat_max = bmax
            obj.berat_min = bmin
            obj.diff = diff
            obj.save()

            return redirect('/berat')
    else:
        form = BeratForm()

    return render(request, 'berat/tambah.html', {'form':form})

def detil(request, data_id):
    obj = Berat.objects.get(pk=data_id)
    obj.diff = obj.berat_max - obj.berat_min
    template = loader.get_template('berat/detil.html')
    context = {
        'obj':obj
    }

    return HttpResponse(template.render(context, request))