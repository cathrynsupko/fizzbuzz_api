from django.db import models


class Fizzbuzz(models.Model):
  fizzbuzz_id = models.AutoField(primary_key=True)
  useragent = models.CharField(max_length=250)
  creation_date = models.DateTimeField(auto_now_add=True)
  message = models.CharField(max_length=140)
  
  class Meta:
    ordering = ('creation_date',)