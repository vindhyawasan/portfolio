from django.contrib import admin
from .models import(
    ContactMessage,
    Experience,
    Project,
    Skill,
    Education,
    Resume,
    Profile
)


admin.site.register(Profile)
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(ContactMessage)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Skill)

# Register your models here.
