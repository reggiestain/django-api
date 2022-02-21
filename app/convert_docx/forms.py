from django import forms  
class UploadFileForm(forms.Form):  
    file      = forms.FileField(label='',
                                widget=forms.ClearableFileInput(attrs={'multiple': True,'class':'hide_broswe'})) # for creating file input  
    class Meta:
        fields = ('file', )  
