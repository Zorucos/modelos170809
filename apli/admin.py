from django.contrib import admin
from .models import Client, Persona, Proyecto, Afectacion

#isma
#<!--from .models import Post

#class PostModelAdmin(admin.ModelAdmin):
#    list_display = ["__unicode__", "timestamp", "updated"]
#    list_display = ["updated"]
#    class Meta:
#        model = Post


#admin.site.register(Post, PostModelAdmin)

#isma

admin.site.register(Client)
admin.site.register(Proyecto)
admin.site.register(Persona)
admin.site.register(Afectacion)
