from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Category
from currency.models import Currency


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_currencies_count', 'related_currencies_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Currency,
                'category',
                'currencies_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Currency,
                'category',
                'currencies_count',
                cumulative=False)
        return qs

    def related_currencies_count(self, instance):
        return instance.currencies_count
    related_currencies_count.short_description = 'Related currencies (for this specific category)'

    def related_currencies_cumulative_count(self, instance):
        return instance.currencies_cumulative_count
    related_currencies_cumulative_count.short_description = 'Related currencies (in tree)'


admin.site.register(Category, CategoryAdmin)
