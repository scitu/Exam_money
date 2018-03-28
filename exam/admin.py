from django.contrib import admin

# Register your models here.
from exam.models import Lac

class LacAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Lac._meta.fields]
admin.site.register(Lac,LacAdmin)

