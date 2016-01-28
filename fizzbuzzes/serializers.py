from rest_framework import serializers
from fizzbuzzes.models import Fizzbuzz

class FizzbuzzSerializer(serializers.ModelSerializer):
  class Meta:
    model= Fizzbuzz
    fields = ('fizzbuzz_id', 'useragent', 'creation_date', 'message')