from django import forms
from .models import Guideline

class GuidelineForm(forms.ModelForm):
	class Meta:
		model = Guideline
		fields = "__all__"
class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)