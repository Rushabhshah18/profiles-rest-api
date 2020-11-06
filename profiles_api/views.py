from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    '''
    Test API View
    '''

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''
        Return a list of APIView Features
        :param request:
        :param format:
        :return:
        '''
        an_apiview = [
            'Uses HTTP methods as Function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self,request):
        '''
        Create a hello message with our name
        :param request:
        :return:
        '''
        serializers = self.serializer_class(data=request.data)
        print("Hello")
        if serializers.is_valid():
            name=serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        '''
        Handle updating an object
        :param request:
        :param pk:
        :return:
        '''

        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        '''
        Handle partial update of a object
        :param request:
        :param pk:
        :return:
        '''
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        '''
        Delete an Object
        :param request:
        :param pk:
        :return:
        '''

        return Response({'method':'DELETE'})