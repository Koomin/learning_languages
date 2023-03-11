from learning_languages.translations.models import Translation, Word
from rest_framework import serializers


class WordSerializer(serializers.ModelSerializer):
    language_name = serializers.CharField(source='language.name', allow_null=True, required=False)
    language_code = serializers.CharField(source='language.code', allow_null=True, required=False)

    class Meta:
        model = Word
        fields = ['uuid', 'word', 'language', 'language_code', 'language_name']


class TranslationSerializer(serializers.ModelSerializer):
    original_word_str = serializers.CharField(source='original_word.word', allow_null=True, required=False)
    original_word_language = serializers.CharField(
        source='original_word.word.language.uuid', allow_null=True, required=False
    )
    original_word_language_name = serializers.CharField(
        source='original_word.word.language.name', allow_null=True, required=False
    )
    translated_word_str = serializers.CharField(source='translated_word.word', allow_null=True, required=False)
    translated_word_language = serializers.CharField(
        source='translated_word.word.language.uuid', allow_null=True, required=False
    )
    translated_word_language_name = serializers.CharField(
        source='translated_word.word.language.name', allow_null=True, required=False
    )

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
