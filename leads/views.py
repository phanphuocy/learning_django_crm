from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead


def index(request):
    leads = Lead.objects.all()
    ctx = {
        'leads': leads
    }
    return render(request, 'leads/index.html', context=ctx)


def show(request, pk):
    lead = Lead.objects.get(id=pk)
    ctx = {
        'lead': lead
    }
    return render(request, 'leads/show.html', context=ctx)
