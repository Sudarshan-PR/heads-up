from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import QueryForm
from .scrape import ScrapeAmzn
# Create your views here.

@login_required
def home(request):
    form = QueryForm()
    return render(request, 'main/home.html', {'form': form})

@login_required
def confirm(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['link']
            scrape = ScrapeAmzn(url)
            price = scrape.getPrice()
            limit = form.cleaned_data['limit']

            return render(request, 'main/confirm.html', {'Product_price': price, 'url': url, 'limit': limit})
            

