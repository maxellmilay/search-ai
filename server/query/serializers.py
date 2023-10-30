from rest_framework import serializers
from .models import Query, LangchainPgEmbedding

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = (
            'uuid',
            'content',
            'vector',
            'created'
        )

class LangchainPgEmbeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LangchainPgEmbedding
        fields = (
            'uuid',
            'collection',
            'embedding',
            'document',
            'cmetadata',
            'custom_id'
        )
