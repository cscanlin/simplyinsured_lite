from django import forms

class ZipAgeForm(forms.Form):
    zip_code = forms.IntegerField(label='Zip Code')
    ages = forms.CharField(label='ages to search for (separated by comma)', max_length=100)
