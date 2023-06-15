from django.contrib import admin
from .models import Tool,Post,About,\
    Project,Service,Category,SocialLink,ProfileDate

# Register your models here.
admin.site.register(Tool)
admin.site.register(Post)
admin.site.register(About)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(SocialLink)

@admin .register(ProfileDate)
class ProfileDateAdmin(admin.ModelAdmin):
    list_display = ("id","full_name")
    search_fields = ("full_name",)
    list_filter = ("created_at","update_at")

