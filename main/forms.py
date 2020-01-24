from django import forms

class QueryForm(forms.Form):
    email = forms.EmailField(label='Enter Your Email ID :', required=True)
    link = forms.URLField(label='Enter the url of the app in steam: ', required=True)
    limit = forms.IntegerField(label='Enter the price limit in US Dollars: ', required=True)