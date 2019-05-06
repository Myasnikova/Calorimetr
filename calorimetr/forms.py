from django import forms

class SearchDishForm(forms.Form):
    q = forms.CharField(widget=forms.TextInput(attrs={
        'size' : 30,
        'class' : 'form-control search-tag-query typeahead',
        'id' : 'typeahead',
        'autofocus' : 'autofocus',
        'placeholder': 'start typing...'
    }))
