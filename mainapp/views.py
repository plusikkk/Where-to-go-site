from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LocationsForm

def main(request):
    return render(request, 'mainapp/main.html')

def addplace(request):
    if request.method == 'POST':
        form = LocationsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            if 'date' in data and data['date'] is not None:
                data['date'] = data['date'].isoformat()

            places = request.session.get('places', [])
            places.append(data)
            request.session['places'] = places
            return redirect('list')
        else:
            print("FORM errors:", form.errors)
    else:
        form = LocationsForm()

    return render(request, 'mainapp/addplace.html', {'form': form})

def listpage(request):
    places = request.session.get('places', [])
    return render(request, 'mainapp/listpage.html', {'locations': places})