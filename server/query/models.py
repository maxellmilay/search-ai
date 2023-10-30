from django.db import models
from pgvector.django import VectorField
import uuid

class Query(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    content = models.TextField()
    vector = VectorField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.uuid)
    
class LangchainPgCollection(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    cmetadata = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'langchain_pg_collection'


class LangchainPgEmbedding(models.Model):
    uuid = models.UUIDField(primary_key=True)
    collection = models.ForeignKey(LangchainPgCollection, models.DO_NOTHING, blank=True, null=True)
    embedding = VectorField(dimensions=1536)
    document = models.CharField(blank=True, null=True)
    cmetadata = models.TextField(blank=True, null=True)
    custom_id = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'langchain_pg_embedding'
