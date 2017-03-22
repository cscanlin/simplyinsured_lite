from django.core import serializers
from django.shortcuts import render

# Create your views here.
from .forms import ZipAgeForm
from .models import Region, Plan, Price

def search(request):
    if request.method == 'POST':
        form = ZipAgeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ages_list = list(map(int, data['ages'].split(',')))
            region = Region.objects.get(zip_code=data['zip_code']).region
            prices = Price.objects.filter(region=region, age__in=ages_list)
            # results = serializers.serialize('json', prices, indent=2)  # for json
            results = prices
    else:
        form = ZipAgeForm()
        results = None

    return render(request, 'search.html', {'form': form, 'results': results})
