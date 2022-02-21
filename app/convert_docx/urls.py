from django.urls import path
from . import views

app_name = 'convert_docx'

urlpatterns = [
    path('upload/', views.upload_pdf_view, name='upload_pdf'),
    path('api/convert/',views.ConvertDocView.as_view(), name='convert'),

]