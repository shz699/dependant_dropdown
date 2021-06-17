from v1.models import Country
from django.shortcuts import render
from .models import Country , City

# Create your views here.
def index(request):
    countries = Country.objects.all() #.order.by('-name')
    cities = City.objects.none()
    if request.method == 'POST':
        country = request.POST['country']
        city = request.POST['city']
        country = Country.objects.get(id= country)
        city = City.objects.get(id= city)
        print(country)
        print(city)
        
    context = {
        'countires':countries,
        'cities':cities,
    }
    return render(request, 'v1/index.html' , context)

def load_cities(request):
    country = request.GET.get('country')
    cities = City.objects.filter(country=country).order_by('name')
    return render(request, 'v1/ajax.html', {'cities': cities})


def error404(request , exception):
    return render(request , 'v1/404.html')    