from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import QueryForm
from .scrape import ScrapeAmzn
import re
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

            urlRegex = re.compile(r'(https://www.amazon.in/.+/dp/.+/)(ref=.+)?')
            mo = urlRegex.search(url)

            if mo is not None:
                scrape = ScrapeAmzn(mo.group(1))
                price = scrape.getPrice()
                limit = form.cleaned_data['limit']

            else:
                msg = "Sorry, currently only https://www.amazon.in urls work!"
                return render(request, 'main/confirm.html', {'message': msg})

            return render(request, 'main/confirm.html', {'Product_price': price, 'url': url, 'limit': limit})
            

