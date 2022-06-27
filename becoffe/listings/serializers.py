from rest_framework import serializers
from listings.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('id','firstName','lastName','email','password','account_type')