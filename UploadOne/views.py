from django.shortcuts import render,redirect
from uploadFiles import settings
from django.core.files.storage import FileSystemStorage

from .models import Document
from .forms import DocumentForm
# Create your views here.

def home(request):
    documents = Document.objects.all()
    return render(request, 'UploadOne/home.html', { 'documents': documents })

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('UploadOne:home')
    else:
        form = DocumentForm()
    return render(request, 'UploadOne/model_form_upload.html', {
        'form': form
    })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'UploadOne/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'UploadOne/simple_upload.html')
