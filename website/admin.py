from django.contrib import admin
from website.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    #fields = ('title',)
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    search_fields = ['name','content']

admin.site.register(Contact)
#admin.site.register(Newsletter)


