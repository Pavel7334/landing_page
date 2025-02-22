from django.contrib import admin
from .models import CmsSlider
from django.utils.safestring import mark_safe


class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_img')
    list_editable = ('cms_css', )
    fields = ('cms_img', 'cms_title', 'cms_text', 'get_img', 'cms_css')
    readonly_fields = ('get_img', )

    def get_img(self, obj):
        if obj.cms_img:
            return mark_safe(f"<img src='{obj.cms_img.url}' width=50>")

    get_img.short_description = 'Изображение'


admin.site.register(CmsSlider, CmsAdmin)
