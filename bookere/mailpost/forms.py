from django import forms

class FakeEmailForm(forms.Form):
    subject = forms.CharField(max_length=100, required=False)
    plain = forms.CharField(label="Message", widget=forms.Textarea, required=False)
    to = forms.CharField(initial="<39b5ef0e6660524333d3@cloudmailin.net>",widget=forms.HiddenInput())
    secret = forms.CharField(initial="9e6a1be956c7ef8aea57",widget=forms.HiddenInput())   
    signature = forms.CharField(widget=forms.HiddenInput(), required=False)
    def __init__(self, user, *args, **kwargs):
        super(FakeEmailForm, self).__init__(*args, **kwargs)
        self.fields['from'] = forms.EmailField(initial=user.email)
