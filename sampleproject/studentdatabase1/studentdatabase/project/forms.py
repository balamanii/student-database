from django import forms
from django.contrib.auth.models import User
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['name', 'roll', 'class_name', 'department', 'subject']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        student = super().save(commit=False)
        student.user = user
        if commit:
            student.save()
        return student





class StudentForm(forms.ModelForm):
        class Meta:
            model = Student
            fields = ['name', 'roll', 'class_name', 'department', 'subject']
