from django.forms import ModelForm
from centers.models import Center


class CenterForm(ModelForm):
    class Meta:
        model = Center
        fields = ['name', 'website', 'email']
    