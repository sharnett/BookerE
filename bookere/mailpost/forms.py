from django import forms
from django.http import HttpResponseServerError


def hideify(field,value):
    field.initial = value
    field.widget = forms.HiddenInput()

class CloudMailinForm(forms.Form):
    subject = forms.CharField(max_length=100, required=False)
    plain = forms.CharField(label="Message", widget=forms.Textarea, required=False)
    to = forms.CharField(max_length=100,required=True, widget=forms.HiddenInput())
    def __init__(self, *args, **kwargs):
        super(CloudMailinForm, self).__init__(*args, **kwargs)
        init_data = kwargs['initial']
        from_field = forms.EmailField()
        secret_field = forms.CharField()

        user = init_data.get('user',None)
        secret = init_data.get('secret',None)

        if user:
            hideify(from_field,user.email)

        if not secret:
            return HttpResponseServerError('need secret for local client', mimetype="text/plain")
        else:
            hideify(secret_field,secret)

        self.fields['from'] = from_field
        self.fields['secret'] = secret_field
