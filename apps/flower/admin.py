from django.contrib import admin

from apps.flower.models import Flower, Sort, Plantation


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('title','price','owner','id')
    readonly_fields = ('views','owner')
    search_fields = ('title',)

    def save_model(self, request, obj, form, change) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)



class FlowerInline(admin.TabularInline):
    readonly_fields = ('views','owner')
    model = Flower
    extra = 2

@admin.register(Sort)
class SortAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    inlines = [FlowerInline]


@admin.register(Plantation)
class PlantationAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    inlines = [FlowerInline]    
