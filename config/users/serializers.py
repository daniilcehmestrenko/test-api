from rest_framework.serializers import CharField, ModelSerializer, ValidationError

from .models import User

class UserRegisterSerializer(ModelSerializer):
    password2 = CharField()

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')

    def save(self):
        data = self.validated_data
        user = User(
                email=data['email'],
                username=data['username'],
            )
        password = data['password']
        password2 = data['password2']

        if password != password2:
            raise ValidationError(
                    {'password2': 'Пароли не совпадают'}
                )
        user.set_password(password)
        user.save()

        return user
