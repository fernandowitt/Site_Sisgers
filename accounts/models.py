from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils.translation import ugettext_lazy as _
import re
from django.utils import timezone

# Create your models here.

class CustomUser(AbstractUser):
	username = models.CharField(_('username'),max_length=15, unique=True, help_text=_('15 caracteres ou menos. Aceita letras, números e @/./+/-/_'), validators=[ validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Insira um usuário válido.'), _('inválido'))])
	first_name = models.CharField(_('first name'), max_length=30, blank=False, null=False)
	last_name = models.CharField(_('last name'), max_length=30, blank=False, null=False)
	email = models.EmailField(_('email address'), max_length=255, unique=True, blank=False, null=False)
	is_staff = models.BooleanField(_('staff status'), default=False, blank = True)
	is_active = models.BooleanField(_('active'), default=True, blank = True)
	is_trusty = models.BooleanField(_('trusty'), default=False, blank = True)
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now, blank = True)
