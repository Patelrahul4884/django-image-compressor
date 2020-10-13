from django.shortcuts import render, redirect,reverse
from django.views import View
from .models import Upload
from .forms import imageUploadForm
from PIL import Image
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request,'size_reducer/home.html')


class MainView(View):
    def get(self,request):
        images=Upload.objects.all()
        imageUploadFormResult = imageUploadForm(request.POST, request.FILES)
        print(images)
        ctx={'images':images,'imageUploadFormResult': imageUploadFormResult}
        return render(request,'size_reducer/size_reducer_list.html',ctx)
    def post(self,request):
        imageUploadFormResult = imageUploadForm(request.POST, request.FILES)
        if imageUploadFormResult.is_valid():
             imageUploadFormResult.save()
             return redirect('size_reducer:all')


def ImageDelete(request,pk):
    success_url='size_reducer:all'
    if request.method=='POST':
        image=Upload.objects.get(id=pk)
        image.delete()
    return redirect(success_url)



