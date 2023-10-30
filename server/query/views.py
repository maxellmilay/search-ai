from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from pgvector.django import L2Distance
from .models import LangchainPgEmbedding
from .embeddings import get_embedding
from .open_ai import answer_query

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

        answer = answer_query(context)
        context['answer'] = answer
        
        return Response(context)

    return Response(
        {"message": "There is no query"},
        status=HTTP_400_BAD_REQUEST
    )
    
