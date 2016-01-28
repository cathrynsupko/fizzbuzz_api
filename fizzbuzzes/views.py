from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fizzbuzzes.models import Fizzbuzz
from fizzbuzzes.serializers import FizzbuzzSerializer

#generate api views for fizzbuzz_list
@api_view(['GET','POST'])
def fizzbuzz_list(request):
  if request.method == 'GET':
    #list all fizzbuzes
    fizzbuzzes = Fizzbuzz.objects.all()
    serializer = FizzbuzzSerializer(fizzbuzzes, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    #create a new fizzbuzz
    data = request.data
    data['useragent'] = request.META.get('HTTP_USER_AGENT')
    serializer = FizzbuzzSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#generate api view for fizzbuzz_detail
@api_view(['GET'])
def fizzbuzz_detail(request, pk):
  try:
    fizzbuzz = Fizzbuzz.objects.get(pk=pk)
  except Fizzbuzz.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = FizzbuzzSerializer(fizzbuzz)
    return Response(serializer.data)
      
    
    

      
    