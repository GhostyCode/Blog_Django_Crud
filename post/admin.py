from django.contrib import admin
from .models import Post, PostView, Comentario, Like, Dislike, Usuario
# Register your models here.


admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comentario)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Usuario)