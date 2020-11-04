from django.contrib.admin import register
from ordered_model.admin import OrderedModelAdmin

# Register your models here.
from pypro.modulos.models import Modulo, Aula


@register(Modulo)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'publico', 'move_up_down_links')
    prepopulated_fields = {'slug': ('titulo',)}


@register(Aula)
class AulaAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'modulo', 'order', 'move_up_down_links')
    list_filter = ('modulo', 'order')
    prepopulated_fields = {'slug': ('titulo',)}
