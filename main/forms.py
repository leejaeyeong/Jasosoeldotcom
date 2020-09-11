from django import forms
from .models import Jasoseol

class JssForm(forms.ModelForm):
    # 어떤 모델과 대응되는 html form 
    class Meta:
        model = Jasoseol
        fields = ('title', 'content',)