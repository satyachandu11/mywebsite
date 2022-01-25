from django.contrib import admin
from Hello.models import Contact
from Hello.models import Quotes

# Register your models here.
admin.site.register(Contact)
admin.site.register(Quotes)