from django import forms

class QueryForm(forms.Form):
    link = forms.URLField(label='Enter the url of the Amazon Product(MUST BE amazon.in): ', required=True)
    limit = forms.IntegerField(label='Enter the price limit in Indian Rupees: ', required=True)