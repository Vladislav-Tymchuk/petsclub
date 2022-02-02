from django.contrib import admin

from relation.models import Followers, LikePost, LikeComment

admin.site.register(Followers)
admin.site.register(LikePost)
admin.site.register(LikeComment)