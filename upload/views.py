# Create your views here.
from upload.models import File, Type

from upload.forms import UploadForm
from django.shortcuts import render

def index(request):
	if request.POST:
		form=UploadForm(request.POST)
		#first split filename through '.', then trim extension
		extension=str(request.FILES['name']).split('.')[-1]
		#creating an instance of File model
		try:
			uploadedFile=File(
				name=request.FILES['name'],
				size=request.FILES['name'].size,
				type=Type.objects.get(ext=extension),
				)
		except Type.DoesNotExist:
			fileTypes = ", ".join(str(fileType) for fileType in Type.objects.all())
			#on unsuccessful upload - filetype not supported
			return render(request, 'upload/index.jade', {'form':form, 'error':'file type not fit for upload, allowed file types: %s' % fileTypes})
		#saving uploaded file to the disk and db
		uploadedFile.save()
		#on successful upload
		return render(request, 'upload/index.jade', {'form':form, 'success':'file uploaded'})
	else:
		#form displaying
		form=UploadForm()
		return render(request, 'upload/index.jade', {'form':form})