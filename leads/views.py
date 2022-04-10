from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import LeadModelForm
from .models import Lead, Agent


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


def new(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')

    ctx = {
        'form': form
    }
    return render(request, 'leads/new.html', context=ctx)


def update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    print (request.method)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("/leads")
        else:
            return HttpResponse('Form is invalid')

    ctx = {
        'form': form,
        'lead': lead
    }
    return render(request, 'leads/update.html', context=ctx)


def delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")