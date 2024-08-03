from django.contrib import admin
from django.contrib import admin
from posts.models import Post
class PostsAdmin(admin.ModelAdmin):
    list_display=("get_category","get_applicants_count","get_company","location","desc","posted_at","is_active")
    
    def get_category(self, obj):
        return obj.category.name
    get_category.short_description = 'Category'
    
    def get_company(self, obj):
        return obj.company.id
    get_category.short_description = 'Company'

    def get_applicants_count(self, obj):
        return obj.applicants.count()
    get_applicants_count.short_description = 'Applicants'
    
admin.site.register(Post , PostsAdmin)
# Register your models here.
