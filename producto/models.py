from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    slug = models.SlugField()
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-fecha_agregado',)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return f'/{self.categoria.slug}/{self.slug}/' 

    def get_image(self):
        if self.imagen:
            return 'http://127.0.0.1:8000' + self.imagen.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.imagen:
                self.thumbnail = self.make_thumbnail(self.imagen)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''  

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail      