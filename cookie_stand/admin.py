from django.contrib import admin
from .models import Cookie_Stand


@admin.register(Cookie_Stand)
class AdminForCookie_Stand(admin.ModelAdmin):
    list_display = ("location", "owner", "created_at")
    # prepopulated_fields = {
    #     "slug": ("title",),
    # }


# admin.site.register(AnotherModel)
