from django.contrib import admin

from home.models import *

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)