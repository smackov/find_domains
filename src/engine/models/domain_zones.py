import logging

from django.db import models


logger = logging.getLogger(__name__)


class DomainZone(models.Model):
    """
    Domain Zone model.
    """

    name = models.CharField(max_length=128, help_text="the name of Domain Zone")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
