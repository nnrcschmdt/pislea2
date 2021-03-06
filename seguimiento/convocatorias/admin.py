from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

from .models import Convocatoria


@admin.register(Convocatoria)
class ConvocatoriaAdmin(admin.ModelAdmin):
    actions = ['no_necesitan_revisión', 'requieren_documentos_para_su_revisión']
    list_display = ('objeto', 'entidad')
    list_filter = ('departamento', 'tipo', 'estatus')
    fieldsets = [
        (None, {'fields': ['slug', 'departamento', 'entidad', 'tipo', 'modalidad', 'objeto', 'enlace_infosicoes', 'estatus',
                           'impugnada', 'notas']}),
        ('D.B.C', {
            'classes': ('collapse',),
            'fields': ['documento']
        }),
        ('Fechas', {
            'classes': ('collapse',),
            'fields': ['publicada', 'presentada']
        }),
        ('Monto', {
            'classes': ('collapse',),
            'fields': ['monto_bob', 'monto_usd', 'monto_eur']
        }),
    ]
    readonly_fields = (
        'departamento', 'entidad', 'slug', 'objeto', 'enlace_infosicoes', 'modalidad', 'tipo', 'añadida', 'publicada',
        'presentada', 'contacto', 'monto_bob', 'monto_usd', 'monto_eur', 'documento')
    save_on_top = True
    search_fields = ('objeto', 'entidad', 'slug')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        obj.revisor = request.user
        obj.revisado = timezone.now()

        super().save_model(request, obj, form, change)

    def no_necesitan_revisión(self, _, queryset):
        queryset.update(estatus=2)

    no_necesitan_revisión.short_description = "Marcar que las Convocatorias seleccionadas no necesitan revisión"

    def requieren_documentos_para_su_revisión(self, _, queryset):
        queryset.update(estatus=3)

    requieren_documentos_para_su_revisión.short_description = "Marcar que las Convocatorias seleccionadas requieren documentos para su revisión"

    def enlace_infosicoes(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.enlace)
