from django.forms import ModelForm
from berat.models import Berat

class BeratForm(ModelForm):
	class Meta:
		model = Berat
		fields = ['berat_max', 'berat_min']