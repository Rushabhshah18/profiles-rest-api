from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    '''
    Searlizers a name field for testing out API View
    '''
    name = serializers.CharField(max_length=10)
