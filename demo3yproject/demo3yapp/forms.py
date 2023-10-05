from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . models import Record

class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    first_name=forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'FirstName'}))
    last_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'LastName'}))

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


#Create ADD Record Form
class AddRecordForm(forms.ModelForm):
    first_name=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"First Name","class":"form-control"}),label="")
    last_name=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name","class":"form-control"}),label="")
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    gender = forms.ChoiceField(
        label='Gender',
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        initial='',  # Set the initial value to an empty string
    )


    hobbies = forms.MultipleChoiceField(choices=[('reading', 'Reading'), ('writing', 'Writing'), ('music', 'Music')],widget=forms.CheckboxSelectMultiple, required=False)

    email=forms.EmailField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Email","class":"form-control"}),label="")
    # phone=forms.IntegerField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Phone","class":"form-control"}),label="")
    date_of_birth = forms.DateField(
        label='Date of Birth',
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        required=True,

    )

    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter phone number','style':'width:604px;''margin-right:10px;'}),required=True,label="")
    # phone= forms.IntegerField(label="", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    # address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Enter your Address", "class": "form-control",'rows':3,'cols':40}), label="")
    address = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your address',"class":"form-control",'rows':3,'cols':40}),required=True,label="")
    state=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"State","class":"form-control"}),label="")
    from django import forms

    class MyForm(forms.Form):
        DEPARTMENT_CHOICES = [
            ('', 'Select Department'),  # Empty choice
            ('science', 'Science'),
            ('commerce', 'Commerce'),

        ]

        COURSES_CHOICES = [
            ('', 'Select Course'),  # Empty choice
            ('computer', 'Computer'),
            ('biology', 'Biology'),
            ('bba', 'BBA'),
            ('bcom', 'BCOM'),
        ]

        department = forms.ChoiceField(

            label='Department',
            choices=DEPARTMENT_CHOICES,
            required=False,  # You can set it to True if needed


        )

        courses = forms.ChoiceField(
            label='Courses',
            choices=COURSES_CHOICES,
            required=False,

        )
    class Meta:
        model=Record
        exclude=('user',)

    def clean_hobbies(self):
        selected_hobbies=self.cleaned_data.get('hobbies',[])
        formatted_hobbies=",".join(selected_hobbies)
        return formatted_hobbies
