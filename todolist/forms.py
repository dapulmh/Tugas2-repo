from django import forms


class TaskForm(forms.Form):
    title = forms.CharField(widget = forms.TextInput(attrs = {'name':'title'}))
    description = forms.CharField(widget = forms.Textarea(attrs = {'name': 'body'}))
    