from django import forms
from cloudmailin.views import generate_signature

class FakeEmailForm(forms.Form):
    subject = forms.CharField(max_length=100, required=False)
    plain = forms.CharField(label="Message", widget=forms.Textarea, required=False)
    def __init__(self, user, *args, **kwargs):
        super(FakeEmailForm, self).__init__(*args, **kwargs)
        self.fields['from'] = forms.EmailField(initial=user.email)
        self.fields['to'] = forms.CharField(initial="<39b5ef0e6660524333d3@cloudmailin.net>")
        self.fields['secret'] = forms.CharField(initial="9e6a1be956c7ef8aea57")   
# pain in my ass, need to generate a signature based on the message
# this needs to happen after the form is submitted, but before it's passed to cloudmailin
        # params = dict((k, v) for k, v in request.POST.iteritems())
        # self.fields['signature'] = forms.CharField(initial=generate_signature(params, secret))
