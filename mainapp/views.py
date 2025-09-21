from django.shortcuts import render, redirect
import random

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

def place_detail(request, place_id):
    places = request.session.get('places', [])
    try:
        place = places[place_id]
    except IndexError:
        place = None
    return render(request, 'mainapp/places.html', {'place': place})

def random_place(request):
    places = request.session.get('places', [])
    if not places:
        return redirect('list')
    chosen_index = random.choices(
        range(len(places)),
        weights=[p['rating'] for p in places],
        k=1
    )[0]
    return redirect('place_detail', place_id=chosen_index)