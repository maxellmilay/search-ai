from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pgvector.django import L2Distance
from .models import LangchainPgEmbedding
from .embeddings import get_embedding

@api_view(["POST"])
def search_query(request):
    query = request.data.get("query")
    
    if query:
        embedding = get_embedding(query)

        most_similar = LangchainPgEmbedding.objects.order_by(
            L2Distance('embedding', embedding)
        ).first()

        context = {
            'query': query,
            'most_similar': most_similar.document
        }
        
        return Response(context)

    return Response({
        "query": "There is no query",
    })
    
