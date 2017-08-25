from django.contrib import admin
from .models import Client, Project, Attachment, Person, Assignment, Horaire, Cost

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
admin.site.register(Project)
admin.site.register(Attachment)
admin.site.register(Person)
admin.site.register(Assignment)
admin.site.register(Horaire)
admin.site.register(Cost)
