from django import forms
from .models import Guideline

class GuidelineForm(forms.ModelForm):
	class Meta:
		model = Guideline
		fields = "__all__"
