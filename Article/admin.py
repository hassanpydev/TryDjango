from django.contrib import admin

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    search_fields = ["title"]
    list_filter = ["title"]
    list_per_page = 10


from .models import Article

admin.site.register(Article, ArticleAdmin)
