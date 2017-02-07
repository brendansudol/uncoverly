from django.contrib import admin
from django.utils.html import format_html

from web.models import Product, Seller


@admin.register(Product, site=admin.site)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'category', 'preview')
    list_filter = ('state', 'is_awesome', 'is_visible', 'category')
    actions = ('mark_awesome', 'mark_not_awesome')
    ordering = ('rand1',)

    def preview(self, obj):
        return format_html(
            '<a target="_blank" href="https://www.etsy.com/listing/{}">'
            '<img src="{}" style="width:120px;">'
            '</a>',
            obj.pk,
            obj.image_main,
        )

    def set_awesome(value):  # NOQA
        def fn(self, request, qs):
            qs.update(is_awesome=value)
            if not value:
                qs.update(is_visible=value)
        fn.short_description = 'Set is_awesome to {}'.format(value)
        return fn

    mark_awesome = set_awesome(True)
    mark_not_awesome = set_awesome(False)


@admin.register(Seller, site=admin.site)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'num_favorers', 'listings_all_count')
