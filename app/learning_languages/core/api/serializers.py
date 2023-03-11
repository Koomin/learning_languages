from learning_languages.core.models import CoreUser
from rest_framework import serializers


class CoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreUser
        fields = [
            'uuid',
            'username',
            'first_name',
            'last_name',
            'email',
            'groups',
            'translated_words',
            'today_translated_words',
            'daily_limit',
        ]
