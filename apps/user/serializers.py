from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from apps.user.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=300, write_only=True)
    phone = serializers.IntegerField()

    class Meta:
        model = UserModel
        fields = ('fullname', 'phone', 'password')

    def validate_password(self, data):
        return make_password(data)

    def validate_phone(self, data):
        if len(str(data)) != 9:
            raise serializers.ValidationError('Input phone number correctly number rooms == 9')
        return data

    # def validate(self, data):
    #     password = data.get('password')
    #     confirm_password = data.pop('password')
    #
    #     if password != confirm_password:
    #         raise serializers.ValidationError("Wrong password!")
    #     return data

    # def create(self, validated_data):
    #     user = UserModel.objects.create(
    #         fullname=validated_data['fullname'],
    #         phone=validated_data['phone'],
    #         # password=validated_data['password'],
    #         confirm_password=validated_data['confirm_password']
    #     )
    #     return user


