import itertools
from django import forms

from .models import Tag


class TagSelectForm(forms.Form):
    tag = forms.ChoiceField(
        choices=itertools.chain([('all', 'All')],
                                ((tag.id, tag.name) for tag in Tag.objects.all())),
        widget=forms.Select(attrs={'class': 'form-control', 'name': 'tag',
                                    'onchange': 'this.form.submit();'}),
    )
