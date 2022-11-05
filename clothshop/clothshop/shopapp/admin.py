from django.contrib import admin

# Register your models here.
from shopapp.models import Category, Product,PrdtImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)
class PrdtimageAdmin(admin.StackedInline):

    model = PrdtImage
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
    inlines = [PrdtimageAdmin]

admin.site.register(Product,ProductAdmin)
admin.site.register(PrdtImage)
class PrdtimageAdmin(admin.ModelAdmin):
   pass