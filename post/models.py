from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class Usuario(AbstractUser):
    pass

    # def __str__(self):
    #     return self.nombre
    

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    miniatura = models.ImageField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    ultima_actulizacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={
            "slug": self.slug
        })
    
    def get_like_url(self):
        return reverse("like", kwargs={
            "slug": self.slug
        })
    
    def get_dislike_url(self):
        return reverse("dislike", kwargs={
            "slug": self.slug
        })
    
    @property
    def comment(self):
        return self.comentario_set.all()


    @property
    def get_comment_count(self):
        return self.comentario_set.all().count()
    

    @property
    def get_view_count(self):
        return self.postview_set.all().count()

    @property
    def get_like_count(self):
        return self.like_set.all().count()

    @property
    def get_dislike_count(self):
        return self.dislike_set.all().count()
    
class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()

    # def __str__(self):
    #     return self.usuario.nombre

    


class PostView(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.usuario.nombre

class Like(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.usuario.nombre

class Dislike(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.usuario.nombre


