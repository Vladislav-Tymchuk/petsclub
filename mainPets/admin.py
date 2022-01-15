from django.contrib import admin
from .models import Banner, Pet, Post

# Register your models here.
admin.site.register(Banner)
admin.site.register(Pet)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'postSlug': ('postTitle',)}

admin.site.register(Post, PostAdmin)