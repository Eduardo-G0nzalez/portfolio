from django.contrib import admin
from .models import Categoria, Tecnologia, Proyecto, ImagenProyecto, ImagenProyecto2, ImagenProyecto3

class ImagenProyectoInline(admin.TabularInline):
    model = ImagenProyecto
    extra = 1

class ImagenProyecto2Inline(admin.TabularInline):
    model = ImagenProyecto2
    extra = 1

class ImagenProyecto3Inline(admin.TabularInline):
    model = ImagenProyecto3
    extra = 1

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'link_sitio', 'link_repositorio')
    inlines = [ImagenProyectoInline, ImagenProyecto2Inline, ImagenProyecto3Inline]

admin.site.register(Categoria)
admin.site.register(Tecnologia)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(ImagenProyecto)
admin.site.register(ImagenProyecto2)
admin.site.register(ImagenProyecto3)