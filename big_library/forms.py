from django import forms
from django.forms import ModelForm, BooleanField

from big_library.models import Article


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class DocumentSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=255)


class ArticleForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'content']
