from rest_framework import serializers

class piyushlmsSignupSerializer(serializers.Serializer):
    userName = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    number = serializers.IntegerField()
    password = serializers.CharField(max_length=20)
    userType = serializers.CharField(max_length=20)
    gender = serializers.CharField(max_length=20,allow_null=True,
                                   allow_blank=True)
    
    class piyushlmsUpdateEmailSerializer(serializers.Serializer):
        email = serializers.EmailField()
        number = serializers.IntegerField()
        
