from django import forms
from .models import ArticleColumn


class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArtcileColumn
        fields = ('column',)