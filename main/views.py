from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import UserInputs, Check
from .forms import QueryForm
from .scrape import ScrapeAmzn
import re
# Create your views here.
url = limit = price = None

@login_required
def home(request):
    form = QueryForm()
    return render(request, 'main/home.html', {'form': form})

@login_required
def confirm(request):
    global url, limit, price
    if request.method == 'POST':
        if 'confirm' in request.POST:
            form = QueryForm(request.POST)
            if form.is_valid():
                url = form.cleaned_data['link']

                urlRegex = re.compile(r'(https://www.amazon.in(/.+)*/dp/.+/?)(ref=.+)?')
                mo = urlRegex.search(url)

                if mo is not None:
                    url = mo.group(1)
                    scrape = ScrapeAmzn(mo.group(1))
                    price = scrape.getPrice()
                    name = scrape.getProductName()
                    limit = form.cleaned_data['limit']

                else:
                    messages.error(request, "Sorry, currently only https://www.amazon.in urls work!")
                    return redirect('home')

                email = request.user.email
                return render(request, 'main/confirm.html', {'Product_price': price, 'Product_name':name, 'url': url, 'limit': limit, 'email': email})

        elif '_go' in request.POST:
            email = request.user.email

            if (url, email) in list(UserInputs.objects.values_list('url','email_id')):
                messages.error(request, 'This product has already exists!')
                return redirect('home')

            u = UserInputs(email_id=email, url=url, limit=limit)
            u.save()

            if url not in list(Check.objects.values_list('url', flat=True)):
                c = Check(url=url, prices=price)
                c.save()
                
            messages.success(request, f'URL "{url}" successfully added! ')
            return redirect('home')



