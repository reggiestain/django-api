
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.reverse import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.utils.decorators import method_decorator
from .forms import UploadFileForm  
from .FileSerializer import FileSerializer
from docx2pdf import convert


class ConvertDocView(APIView):
      "API for getting the training data"
      parser_classes = [FormParser, MultiPartParser]

      def post(self, request, format=None):
          serializer_class = FileSerializer(data=request.data)
          if 'file' not in request.data or not serializer_class.is_valid():
              return Response(status=status.HTTP_400_BAD_REQUEST)
          else:
              #for f in request.data['file']:
              for file in request.FILES.getlist('file'):
                  FileSystemStorage().save(file.name, file)
              '''doc = request.FILES.getlist('file[]')
              for f in doc:
                  FileSystemStorage().url(FileSystemStorage().save(f.name, f))
                  return Response(status=status.HTTP_201_CREATED)'''
              return JsonResponse({'URL': 'xxxx'})
          #form = UploadFileForm()   
          #return render(request,'convert_docx/upload_pdf.html',context={'form':form})

@method_decorator(csrf_exempt, 'dispatch')
def upload_pdf_view(request):
    if request.method == 'POST':
            myfile = request.FILES
            print(myfile['file'])
    else:    
            form = UploadFileForm()   
            return render(request,'convert_docx/upload_pdf.html',context={'form':form})


def ConvertDoddcView(request):
        uploaded_file_url = 'false'
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
                #handle_uploaded_file(request.FILES['file'])
                myfile = request.FILES['file']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                return JsonResponse({'URL': uploaded_file_url})

