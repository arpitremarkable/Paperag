from django.forms import ModelForm
from upload.models import File

class UploadForm(ModelForm):
    
    class Meta:
        model=File
        fields=('name', )