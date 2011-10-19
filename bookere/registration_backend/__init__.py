from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User

from registration import signals


from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _
from registration.backends.simple import SimpleBackend
attrs_dict = {'class': 'required'}

class BookerEBackend(SimpleBackend):

    def register(self,request,**kwargs):
        username, email, password = kwargs['email'], kwargs['email'], kwargs['password']
        User.objects.create_user(username,email,password)

        new_user = authenticate(username=username, password=password)
        login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user

    def get_form_class(self,request):
        return BookerERegistrationForm

    def post_registration_redirect(self,request,user):
        return ('/books/home', (), {})
class BookerERegistrationForm(forms.Form):
        """
    Form for registering a new user account.
    
    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.
    
    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.
    
    """
        email = forms.EmailField(widget=forms.HiddenInput(attrs=dict(attrs_dict,
                                                                   maxlength=75)),
                                 label=_("E-mail"))
        attrs = attrs_dict
        attrs['class'] = 'required txt'
        password = forms.CharField(widget=forms.HiddenInput())


        def clean_email(self):
                    """
        Validate that the supplied email address is unique for the
        site.
        
        """
                    if User.objects.filter(email__iexact=self.cleaned_data['email']):
                        raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
                    return self.cleaned_data['email']
