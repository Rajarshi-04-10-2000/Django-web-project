from django.contrib import admin
#imported Contact from home.models
from home.models import Contact
# Register your models here.
admin.site.register(Contact)
#now copy the name of apps and register in settings of project
