from django.contrib import admin
from django.db.models import Sum,Count
from blog.models import Post,Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','create_at','like_count')
    def like_count(self,obj):
        return (Post.objects
        .filter(id=obj.id)
        .aggregate(likes_count=Count('like'))['likes_count'])
# class CommentAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Comment)