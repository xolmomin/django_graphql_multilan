from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    re_path(r'^graphql$', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
