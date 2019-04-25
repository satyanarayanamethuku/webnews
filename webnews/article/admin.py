from django.contrib import admin
from .models import Reporter, Aritcle

# Register your models here.
class ArticleDetaile(admin.ModelAdmin):
    list_display=('id','heading','created','reporter','image','body')
    search_fields=('heading','created','body','reporter__name')
admin.site.register(Aritcle,ArticleDetaile)




class ReporterDetaile(admin.ModelAdmin):
    list_display=('id','name')
    search_fields=('name',)
    
admin.site.register(Reporter,ReporterDetaile)


