from django.contrib import admin
from .models import Carrera, Lead, Interaccion

class InteraccionInline(admin.TabularInline):
    model = Interaccion
    extra = 1
    fields = ('tipo', 'notas', 'fecha', 'usuario')
    ordering = ('-fecha',)

@admin.register(Interaccion)
class InteraccionAdmin(admin.ModelAdmin):
    list_display = ('lead', 'tipo', 'fecha', 'usuario', 'notas_cortas')
    list_filter = ('tipo', 'fecha', 'usuario')
    search_fields = ('lead__nombre', 'lead__apellido', 'notas')
    date_hierarchy = 'fecha'

    def notas_cortas(self, obj):
        return obj.notas[:50] + '...' if len(obj.notas) > 50 else obj.notas
    notas_cortas.short_description = 'Notas'

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'activa', 'conteo_aspirantes')
    list_filter = ('activa',)
    search_fields = ('nombre', 'codigo')

    def conteo_aspirantes(self, obj):
        return obj.aspirantes.count()
    conteo_aspirantes.short_description = 'Interesados'

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_completo', 
        'estado_coloreado', 
        'carrera_interes', 
        'telefono', 
        'origen', 
        'fecha_creacion'
    )
    
    list_display_links = ('nombre_completo',)
    
    list_filter = (
        'estado', 
        'carrera_interes', 
        'origen', 
        'fecha_creacion'
    )
    
    search_fields = (
        'nombre', 
        'apellido', 
        'email', 
        'telefono', 
        'colegio'
    )
    
    date_hierarchy = 'fecha_creacion'
    
    readonly_fields = ('fecha_creacion', 'ultima_actualizacion')

    inlines = [InteraccionInline]

    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'apellido', 'email', 'telefono')
        }),
        ('Información Académica', {
            'fields': ('colegio', 'dir_colegio', 'carrera_interes')
        }),
        ('Estado y Seguimiento', {
            'fields': ('estado', 'origen', 'fecha_creacion', 'ultima_actualizacion')
        }),
    )

    def nombre_completo(self, obj):
        return f"{obj.nombre} {obj.apellido}"
    nombre_completo.short_description = 'Aspirante'
    nombre_completo.admin_order_field = 'nombre'

    def estado_coloreado(self, obj):
        from django.utils.html import format_html
        colors = {
            'NUEVO': 'blue',
            'CONTACTADO': 'orange',
            'INTERESADO': 'purple',
            'POSTULANTE': 'teal',
            'MATRICULADO': 'green',
            'PERDIDO': 'red',
        }
        color = colors.get(obj.estado, 'black')
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.get_estado_display()
        )
    estado_coloreado.short_description = 'Estado'