from django.db import models

from misc.utils import get_unique_slug

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    cik_number = models.CharField(max_length=100, unique=True)
    
    class Meta:
        unique_together = ('slug', 'cik_number')
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
            models.Index(fields=['cik_number']),
        ]
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, "name")
        super(Company, self).save(*args, **kwargs)

class RevenueFiling(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    # Timestamp usually works montly for Revenue Filings
    timestamp = models.DateTimeField()
    
    revenue = models.FloatField(null=True, blank=True)
    
    class Meta:
        unique_together = ('company', 'timestamp')
    
    def __str__(self):
        return f'{self.company.name} {self.revenue}'

class EbitdaFiling(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    # Timestamp usually works Yearly for Ebitda Filings
    start_timestamp = models.DateTimeField(default=None, null=True, blank=True)
    end_timestamp = models.DateTimeField(default=None, null=True, blank=True)
    
    ebitda = models.FloatField(null=True, blank=True)
    
    class Meta:
        unique_together = ('company', 'start_timestamp', 'end_timestamp')
    
    def __str__(self):
        return f'{self.company.name} {self.ebitda}'