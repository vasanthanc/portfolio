from django import forms

class ContactMeFrom(forms.Form):
    contact_name = forms.CharField(
        widget=forms.TextInput(attrs={'name':'name', 'id':'name', 'type':'text',
                                      'class':'col-xs-12 col-sm-12 col-md-12 col-lg-12','placeholder':'Your name...'}),
                                   required=True)
    contact_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'name':'email', 'id':'mail',
                                       'type':'email', 'class':'col-xs-12 col-sm-12 col-md-12 col-lg-12 noMarr',
                                       'placeholder':'Email Address...'}),
        required=True)
    content = forms.CharField(
        widget=forms.Textarea(attrs={'name': 'comments', 'id': 'comments', 'cols': '', 'rows': '',
                                      'class': 'col-xs-12 col-sm-12 col-md-12 col-lg-12',
                                      'placeholder': 'Project Details...'}),
        required=True,
    )