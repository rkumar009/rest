from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User)
	phone = models.CharField(max_length=30, blank=True)
	is_new = models.BooleanField(default=True)
	last_seen = models.DateTimeField(null=True, blank=True,
        help_text="The time when the user was last seen on the platform."
                  " Updated on every request.",
        db_index=True)