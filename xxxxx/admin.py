from django.contrib import admin
from .models import Xxxxx


@admin.register(Xxxxx)
class AdminForXxxxx(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    # prepopulated_fields = {
    #     "slug": ("title",),
    # }


# admin.site.register(AnotherModel)
