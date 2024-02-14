from django.contrib import admin
from blog.models import Post,Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "_empty_"
    #fields = ('title',)
    list_display = ('title','counted_views','status','published_date')
    list_filter = ('status',)

admin.site.register(Category)
admin.site.register(Post,PostAdmin)






