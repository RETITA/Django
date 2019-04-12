from django import forms

class CommentForm(forms.Form):
    pseudo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail = forms.EmailField(label="Votre adresse e-mail", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    