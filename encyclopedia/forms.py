from django import forms

class NewPage(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control col-md-4',
            'maxlength': '20',
            'title': 'Enter Markdown Content:', 
            'required': True
        }
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs = {
        'class': 'form-control col-md-10',
        'rows': 10,        
        'title': 'Enter Markdown Content:', 
        'required': True
        }
    ))

class EditPage(forms.Form):
    content = forms.CharField(widget=forms.Textarea(
        attrs = {
        'class': 'form-control col-md-10',
        'rows': 10, 
        'title': 'Enter Markdown Content:', 
        'required': True
        }
    ))