from django import forms
from .models import Project, Contact

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'deploy_url', 'github_url', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Adding specs to the input fields
        self.fields['title'].widget.attrs.update({'class': 'input-field', 'placeholder': 'Project Title'})
        self.fields['deploy_url'].widget.attrs.update({'class': 'input-field', 'placeholder': 'Deploy Url'})
        self.fields['github_url'].widget.attrs.update({'class': 'input-field', 'placeholder': 'GitHub Url'})
        self.fields['description'].widget.attrs.update({'class': 'input-field', 'placeholder': 'Description'})
        self.fields['image'].widget.attrs.update({'class': 'input-field', 'placeholder': 'Project Image'})


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Name', 'autocomplete': 'off', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email', 'autocomplete': 'off', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Phone', 'autocomplete': 'off', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'input-field input-field-message', 'placeholder': 'Message', 'autocomplete': 'off', 'required': True}),
        }