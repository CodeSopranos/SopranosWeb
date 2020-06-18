from django.contrib import admin
from django.db.models import Max, F
from .models import *


from .models import *


class DashboardAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    # def get_queryset(self, request):
    #     return super().get_queryset(request).annotate(updated_at=Max('post__updated_at'))

    def created_at(self, obj):
        return obj.created_at
    created_at.admin_order_field = 'created_at'

    list_display = ('name', 'theme', 'owner')
    ordering = ('name',)
    fields = ('owner', 'name', 'created_at', 'private')
    readonly_fields = ('created_at', 'owner')
    view_on_site = True
    # inlines = (PostInline,)


admin.site.register(Dashboard, DashboardAdmin)
admin.site.register(Figure)
