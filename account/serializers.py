from rest_framework import serializers

from .models import User

class RegisterUserSerializer(serializers.ModelSerializer):  
    password_confirm = serializers.CharField(min_length=4, required=True)


    class Meta:
        model = User
        fields = ('email','password', 'password_confirm')

    def validate(self, attrs):
        # attrs = {'email':some@gmsil.com', 'password':'214235346', 'password_confirm:24234}
        pass1 = attrs.get('password')
        pass2 = attrs.pop('password_confirm')
        if pass1!=pass2:
            raise serializers.ValidationError('Password do not math')
        return attrs

    def validate_email(self,email):
        # email = 'some@gmail.com'
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('user with this email already exists')
        return email

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
