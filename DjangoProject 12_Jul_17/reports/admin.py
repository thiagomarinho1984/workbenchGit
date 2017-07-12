from django.contrib import admin
from .workbench import VESSEL, HULL, PROPELLER, RF, RB, DESIGN, REPORT

# Register your models here.
admin.site.register(VESSEL)
admin.site.register(HULL)
admin.site.register(PROPELLER)
admin.site.register(RF)
admin.site.register(RB)
admin.site.register(DESIGN)
admin.site.register(REPORT)