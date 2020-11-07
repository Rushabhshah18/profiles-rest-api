from rest_framework import serializers
from profiles_api.models import UserProfile


class HelloSerializer(serializers.Serializer):
    '''
    Searlizers a name field for testing out API View
    '''
    name = serializers.CharField(max_length=10)


class UserProfileSearlizer(serializers.ModelSerializer):
    '''
    Searlizes a user profile object
    '''

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        '''
        Create and return a new User
        :param validated_data:
        :return:
        '''
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        '''
        Handle updating user acoount
        :param instance:
        :param validated_data:
        :return:
        '''
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance,validated_data)