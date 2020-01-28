from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import UserInputs, Check
from .forms import QueryForm
from .scrape import ScrapeAmzn
import re
# Create your views here.
url = limit = None

@login_required
def home(request):
    form = QueryForm()
    return render(request, 'main/home.html', {'form': form})

@login_required
def confirm(request):
    global url, limit
    if request.method == 'POST':
        if 'confirm' in request.POST:
            form = QueryForm(request.POST)
            if form.is_valid():
                url = form.cleaned_data['link']

                urlRegex = re.compile(r'(https://www.amazon.in/.+/dp/.+/)(ref=.+)?')
                mo = urlRegex.search(url)

                if mo is not None:
                    url = mo.group(1)
                    scrape = ScrapeAmzn(mo.group(1))
                    price = scrape.getPrice()
                    limit = form.cleaned_data['limit']

                else:
                    msg = "Sorry, currently only https://www.amazon.in urls work!"
                    return render(request, 'main/confirm.html', {'message': msg})

                email = request.user.email
                return render(request, 'main/confirm.html', {'Product_price': price, 'url': url, 'limit': limit, 'email': email})

        elif '_go' in request.POST:
            u = UserInputs(email_id=request.user.email, url=url, limit=limit)
            u.save()

            
            messages.success(request, f'URL "{url}" successfully added! ')
            return redirect('home')



