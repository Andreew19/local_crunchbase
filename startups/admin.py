from django.contrib import admin
from .models import Articles,Categories,Startups,TagGroups,Tags

# Register your models here.



admin.site.register(Articles)
admin.site.register(Categories)
admin.site.register(Startups)
admin.site.register(TagGroups)
admin.site.register(Tags)

