from django.shortcuts import render

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Kk-m-as in el de tutorial!")


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company, Contact
from .forms import CompanyForm, ContactForm


def home(request):
    companies = Company.objects.all()[:5]  # Show last 5 companies
    contacts = Contact.objects.all()[:5]  # Show last 5 contacts
    return render(request, 'home.html', {
        'companies': companies,
        'contacts': contacts
    })


def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Companie adaugata cu succes!')
            return redirect('home')
    else:
        form = CompanyForm()

    return render(request, 'add_company.html', {'form': form})


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact adaugat cu succes!')
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'add_contact.html', {'form': form})