import logging

from django.db import models
from django.utils import timezone


logger = logging.getLogger(__name__)


class Domain(models.Model):
    """
    Domain - the general model in this project.
    """

    name = models.CharField(primary_key=True, max_length=128, help_text="The full domain name")
    domain_zone = models.ForeignKey('DomainZone', on_delete=models.PROTECT)

    whois_check_result = models.BooleanField(blank=True, null=True, help_text="Does exist in whois?")
    whois_check_date = models.DateField(blank=True, null=True, help_text="The date of last whois check")

    resolve_check_result = models.BooleanField(blank=True, null=True, help_text="Can domain be resolved?")
    resolve_check_date = models.DateField(blank=True, null=True, help_text="The date of last resolve attempt")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def update_resolve_check_information(self, result: bool) -> None:
        """
        Set the result of domain resolve checking.
        """
        logger.debug(f'{self.name}: set request result={result}')
        self.resolve_check_result = result
        self.resolve_check_date = timezone.now().date()
        self.save(update_fields=['resolve_check_result', 'resolve_check_date'])
