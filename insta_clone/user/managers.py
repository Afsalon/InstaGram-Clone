from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**kwargs):
        if not email:
            raise ValueError(ugettext_lazy('This email must be set'))
        email=self.normalize_email(email)
        user=self.model(email=email,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password, **kwargs):
        kwargs.setdefault('is_active',True)
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_superuser',True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(ugettext_lazy('staff status was not set'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(ugettext_lazy('superuser status was not set'))
        return self.create_user(email,password,**kwargs)
