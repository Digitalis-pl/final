from django import forms
from django.forms import ModelForm, BooleanField

from big_library.models import Article


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class DocumentSearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=255)


class ArticleForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Article
        fields = ['rubrics', 'title', 'description', 'text',]
