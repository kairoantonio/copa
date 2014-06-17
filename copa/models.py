from django.db import models

class Copa(models.Model):
  gols1 = models.IntegerField(max_length='2', blank=False, null=False)
  gols2 = models.IntegerField(max_length='2', blank=False, null=False)
  gols3 = models.IntegerField(max_length='2', blank=False, null=False)
  gols4 = models.IntegerField(max_length='2', blank=False, null=False)
  gols5 = models.IntegerField(max_length='2', blank=False, null=False)
  gols6 = models.IntegerField(max_length='2', blank=False, null=False)