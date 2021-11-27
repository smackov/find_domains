from django.db import models


class Domain(models.Model):
    """
    Domain - model.
    """
    name = models.CharField(max_length=15)
    full_domain_name = models.CharField(max_length=25)

    whois_check_result = models.BooleanField(blank=True, null=True, help_text="Does exist in whois?")
    whois_check_date = models.DateField(blank=True, null=True, help_text="The date of last whois check")

    request_check_result = models.BooleanField(blank=True, null=True, help_text="Does domain have site?")
    request_check_date = models.DateField(blank=True, null=True, help_text="The date of last request check")

    class Meta:
        ordering = ['full_domain_name']

    def __str__(self):
        return (f'{self.full_domain_name}: '
                f'whois={self.whois_check_result}, '
                f'request={self.request_check_result}')
