 
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User

from django.core import validators
from django import forms
from .models import Application, CertificateDocuments, CertificateEducational, Contact, MastersDocuments, MastersEducational, Other, Status, WorkExperience, Documents

from django import forms

class ProgramTypeForm(forms.Form):
    CHOICES = [
        ('masters', 'Masters'),
        ('certificate', 'Certificate')
    ]
    application_type = forms.ChoiceField(choices=CHOICES, label="Choose Program Type")


class PersonalInfoForm(forms.ModelForm):
    
    class Meta:
        model = Application
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'national_id', 'title', 'marital_status', 'place_of_birth', 'citizenship', 'country', 'disability', 'disability_details']
        
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            
        }
        
        
        
class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['id_document', 'birth_certificate'] 


class ContactAndAddressForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['phone_number', 'email', 'permanent_address_no_street', 'permanent_address_apt_unit', 'permanent_address_state_province', 'home_phone', 'office_phone']


class EducationalBackgroundMastersForm(forms.ModelForm):
    class Meta:
        model = MastersEducational
        fields = ['awarding_institution', 'degree_diploma_level_classification', 'major_subjects', 'date_awarded','programme_applied_for',  'preferred_learning_format', 'prospective_sponsors']
        
        widgets = {
            'date_awarded': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'prospective_sponsors': forms.TextInput(attrs={'placeholder': 'e.g. self'}),
            'degree_diploma_level_classification': forms.TextInput(attrs={'placeholder': 'e.g. Upper Second Class'}),
        }
        
class MastersEducationalDocumentForm(forms.ModelForm):
    class Meta:
        model= MastersDocuments
        fields = ['transcript','degree_certificate', 'CV', 'a_level_certificate', 'o_level_certificate']


class EducationalBackgroundCertificateForm(forms.ModelForm):
    class Meta:
        model = CertificateEducational
        fields = ['period_of_study','institution_attended','level_of_study','major_subjects','date_awarded','programme_applied_for', 'preferred_learning_format', 'prospective_sponsors']
        
    
        widgets = {
            'prospective_sponsors': forms.TextInput(attrs={'placeholder': 'e.g. self'}),
        }
        
        
class CertificateEducationalDocumentForm(forms.ModelForm):
    class Meta:
        model= CertificateDocuments
        fields = ['a_level_certificate', 'o_level_certificate', 'CV']

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = [
            'employer',
            'work_details',
            'work_experience_from',
            'work_experience_to',
            'reference_1_name',
            'reference_1_email',
            'reference_1_phone_number',
            'reference_2_name',
            'reference_2_email',
            'reference_2_phone_number'
        ]

    def __init__(self, *args, **kwargs):
        super(WorkExperienceForm, self).__init__(*args, **kwargs)
    
        for field_name in self.fields:
            self.fields[field_name].required = True

    def clean(self):
        cleaned_data = super().clean()
        
        
        
        
        
        
        
        
        
        
        work_experience_from = cleaned_data.get('work_experience_from')
        work_experience_to = cleaned_data.get('work_experience_to')

        if work_experience_from and work_experience_to:
            if work_experience_from > work_experience_to:
                raise forms.ValidationError("The start date cannot be after the end date.")
        
        
        return cleaned_data


class OtherInfoForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = ['how_did_you_hear_about_ALMA', 'additional_remarks']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']





class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    
        self.error_messages['invalid_login'] = (
            'Invalid username or password.'
        )
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })


class UserRegistrationForm(forms.ModelForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username'}),
            label='Username',
            help_text=None,
            )
    
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email : Example@gmail.com'}),
            label='Email',
            help_text=None,
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password must contain at least one uppercase, lower case letter, and one special character', 'class': 'moving-placeholder'}), 
            label= 'Enter Password',
            help_text=None,
            )
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Cornfirm password'}),
            label='Cornfirm Password',
            help_text=None,
            )
           
    
    
    
    

    class Meta:
        model = User
        fields = ['username', 'email']
        
       
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")




class ResetPasswordForm(PasswordResetForm):
    class Meta:
        model = User
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email',
            'required': 'True'
        })


class ResetPasswordConfirmForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(ResetPasswordConfirmForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'New Password',
            'required': 'True'
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Retype New Password',
            'required': 'True'
        })
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''
        
class ApplicationFilterForm(forms.Form):
    application_id = forms.IntegerField(required=False, label='Application ID')
    status = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'All'),  
            ('Pending', 'Pending'),
            ('Under Review', 'Under Review'),
            ('Accepted', 'Accepted'),
            ('Rejected', 'Rejected'),
        ],
        label='Status'
    )
