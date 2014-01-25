from django.db import models
from django import forms
from django.forms import fields, util
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

errors_msg = {
    'required': 'This field is required',
    'invalid': 'This is an invalid value'
}

class Join(models.Model):
    first_name = models.CharField(max_length=20, null=False, blank=False, error_messages=errors_msg)
    last_name = models.CharField(max_length=20, null=False, blank=False, error_messages=errors_msg)
    email = models.EmailField(null=False, blank=False, error_messages=errors_msg)
    zip_code = models.IntegerField(default=1, null=False, blank=False, error_messages=errors_msg)
    receive_newsletter = models.BooleanField()
    time_stamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.email