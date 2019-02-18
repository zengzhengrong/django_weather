from django.forms import ModelForm,TextInput,ValidationError
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name':TextInput(attrs={'class':'input','placeholder':'City Name'})}

    def clean_name(self):
        name = self.cleaned_data.get('name').strip()
        if City.objects.filter(name=name).exists():
            raise ValidationError('The city name have been in records , you can refresh the page to see the new weather', code='invalid')
        return name