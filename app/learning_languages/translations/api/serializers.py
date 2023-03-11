from learning_languages.core.models import CoreUser
from learning_languages.languages.models import Language
from learning_languages.translations.models import Translation, Word
from rest_framework import serializers


class WordSerializer(serializers.ModelSerializer):
    language_name = serializers.CharField(source='language.name', allow_null=True, required=False)
    language_code = serializers.CharField(source='language.code', allow_null=True, required=False)
    language = serializers.SlugRelatedField(slug_field='uuid', queryset=Language.objects.all(), required=False)

    class Meta:
        model = Word
        fields = ['uuid', 'word', 'language', 'language_code', 'language_name']


class UsersRelatedSerializer(serializers.RelatedField):
    # TODO Finish serializer
    queryset = CoreUser.objects.all()

    def to_representation(self, value):
        return value.uuid


class TranslationSerializer(serializers.ModelSerializer):
    original_word = serializers.SlugRelatedField(slug_field='uuid', queryset=Word.objects.all(), required=False)
    original_word_str = serializers.CharField(source='original_word.word', allow_null=True, required=False)
    original_word_language = serializers.CharField(
        source='original_word.language.uuid', allow_null=True, required=False
    )
    original_word_language_name = serializers.CharField(
        source='original_word.language.name', allow_null=True, required=False
    )
    translated_word = serializers.SlugRelatedField(slug_field='uuid', queryset=Word.objects.all(), required=False)
    translated_word_str = serializers.CharField(source='translated_word.word', allow_null=True, required=False)
    translated_word_language = serializers.CharField(
        source='translated_word.language.uuid', allow_null=True, required=False
    )
    translated_word_language_name = serializers.CharField(
        source='translated_word.language.name', allow_null=True, required=False
    )
    users = UsersRelatedSerializer(many=True, required=False)

    class Meta:
        model = Translation
        fields = [
            'uuid',
            'original_word',
            'original_word_str',
            'original_word_language',
            'original_word_language_name',
            'translated_word',
            'translated_word_str',
            'translated_word_language',
            'translated_word_language_name',
            'users',
        ]
