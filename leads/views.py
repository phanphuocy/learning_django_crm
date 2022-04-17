from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import LeadModelForm
from .models import Lead, Agent


class LeadListView(ListView):
    template_name = "leads/index.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


def index(request):
    leads = Lead.objects.all()
    ctx = {
        'leads': leads
    }
    return render(request, 'leads/index.html', context=ctx)


class LeadDetailView(DetailView):
    template_name = "leads/show.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


def show(request, pk):
    lead = Lead.objects.get(id=pk)
    ctx = {
        'lead': lead
    }
    return render(request, 'leads/show.html', context=ctx)


class LeadCreateView(CreateView):
    template_name = "leads/new.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:list_index")


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


class LeadUpdateView(UpdateView):
    template_name = "leads/update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_index")


def update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    print(request.method)
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


class LeadDeleteView(DeleteView):
    template_name = "leads/delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead_index")


def delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
