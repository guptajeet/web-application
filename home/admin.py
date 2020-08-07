from django.contrib import admin

# Register your models here.
from home.models import Contact, Blog, Books

admin.site.register(Contact)


class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("css/main.css,")
        }

        js = ("js/blog.js",)


admin.site.register(Blog, BlogAdmin)

admin.site.register(Books)

