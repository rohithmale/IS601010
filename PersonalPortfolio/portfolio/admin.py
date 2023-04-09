from django.contrib import admin
from .models import Project,WorkExperience,Education,Skill
# Register your models here.
admin.site.register(Project)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Skill)
