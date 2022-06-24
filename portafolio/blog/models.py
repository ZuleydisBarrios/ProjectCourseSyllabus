from tabnanny import verbose
from django.db import models

from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    author = models.CharField( _('Author'), max_length=55)
    title = models.CharField(_('Titulo'), max_length=55)
    description = models.TextField(_('Descripcion'))
    image = models.ImageField(_('Imagen'),upload_to= "imagen/blog")
    create_at = models.DateTimeField( _('Fecha de creacion'), auto_now_add=True)
    update_at = models.DateTimeField(_('Fecha de actualizacion'), auto_now=True)

    class Meta:
        verbose_name = _('Blog Personality')
        verbose_name_plural = _('Blog personal')

    def __str__(self) -> str:
        return self.author
