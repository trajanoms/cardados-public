from django.contrib import admin
from .models import *

admin.site.register(InspectionGroup)
admin.site.register(InspectionItem)
admin.site.register(InspectionTemplate)
admin.site.register(Inspection)
admin.site.register(InspectionResponse)


