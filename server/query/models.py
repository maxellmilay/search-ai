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
