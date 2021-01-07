from django import forms

class Student(forms.Form):
    name=forms.CharField(max_length=200)
    age=forms.IntegerField(max_value=50)